# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import datetime
import math
import re

from ast import literal_eval
from collections import defaultdict
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _, Command
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_round

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    extra_cost = fields.Float(copy=False, string='Extra Unit Cost')
    show_valuation = fields.Boolean(compute='_compute_show_valuation')


    @api.constrains('move_byproduct_ids')
    def _check_byproducts(self):
        for order in self:
            if any(move.cost_share < 0 for move in order.move_byproduct_ids):
                raise ValidationError(_("By-products cost shares must be positive."))
            # if sum(order.move_byproduct_ids.mapped('cost_share')) > 100:
            #     raise ValidationError(
            #         _("The total cost share for a manufacturing order's by-products cannot exceed 100."))

    def _cal_price(self, consumed_moves):
        """Set a price unit on the finished move according to `consumed_moves`.
        """
        super(MrpProduction, self)._cal_price(consumed_moves)
        work_center_cost = 0
        finished_move = self.move_finished_ids.filtered(
            lambda x: x.product_id == self.product_id and x.state not in ('done', 'cancel') and x.quantity > 0)
        if finished_move:
            finished_move.ensure_one()
            for work_order in self.workorder_ids:
                work_center_cost += work_order._cal_cost()
            quantity = finished_move.product_uom._compute_quantity(
                finished_move.quantity, finished_move.product_id.uom_id)
            extra_cost = self.extra_cost * quantity
            total_cost = - sum(consumed_moves.sudo().stock_valuation_layer_ids.mapped('value')) + work_center_cost + extra_cost 
            byproduct_moves = self.move_byproduct_ids.filtered(lambda m: m.state not in ('done', 'cancel') and m.quantity > 0)
            byproduct_cost_share = 0
            for byproduct in byproduct_moves:
                if byproduct.cost_share == 0:
                    continue
                byproduct_cost_share += byproduct.cost_share 
                if byproduct.product_id.cost_method in ('fifo', 'average'):
                    byproduct.price_unit = byproduct.cost_share / byproduct.product_uom._compute_quantity(byproduct.quantity, byproduct.product_id.uom_id)
            if finished_move.product_id.cost_method in ('fifo', 'average'):
                finished_move.price_unit = (total_cost - byproduct_cost_share) / quantity
        return True
