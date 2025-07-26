# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from odoo import api, Command, fields, models

class StockMove(models.Model):
    _inherit = "stock.move"


    cost_share = fields.Float("Cost Share")

    def _get_price_unit(self):
        price_unit = super()._get_price_unit()

    # Don't override for subcontracting / special flows to avoid breaking SVL
        #if self.production_id and self.production_id.subcontracting:
            #return price_unit

        if self.product_id == self.purchase_line_id.product_id or not self.bom_line_id:
            return price_unit

        cost_share = self.bom_line_id._get_cost_share()

    # Make sure cost_share is float
        if isinstance(cost_share, (int, float)):
            return cost_share
        return price_unit

    @api.onchange('quantity_done')
    def _onchange_quantity_done(self):
        if self.production_id:
            if self.production_id.bom_id:
                mrp_bom_byproduct_id = self.env['mrp.bom.byproduct'].sudo().search([('bom_id', '=', self.production_id.bom_id.id), ('product_id', '=', self.product_id.id)], limit=1)
                if mrp_bom_byproduct_id:
                    self.cost_share = float(mrp_bom_byproduct_id.cost_share)
