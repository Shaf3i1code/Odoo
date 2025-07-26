# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _, Command
from odoo.exceptions import UserError, ValidationError


class MrpByProduct(models.Model):
    _inherit = "mrp.bom.byproduct"

    cost_share = fields.Float("Cost Share")


class MrpBom(models.Model):
    """ Defines bills of material for a product or a product template """
    _inherit = 'mrp.bom'

    @api.constrains('product_id', 'product_tmpl_id', 'bom_line_ids', 'byproduct_ids', 'operation_ids')
    def _check_bom_lines(self):
        for bom in self:
            for bom_line in bom.bom_line_ids:
                if bom.product_id:
                    same_product = bom.product_id == bom_line.product_id
                else:
                    same_product = bom.product_tmpl_id == bom_line.product_id.product_tmpl_id
                if same_product:
                    raise ValidationError(
                        _("BoM line product %s should not be the same as BoM product.") % bom.display_name)
            apply_variants = bom.bom_line_ids.bom_product_template_attribute_value_ids | bom.operation_ids.bom_product_template_attribute_value_ids | bom.byproduct_ids.bom_product_template_attribute_value_ids
            if bom.product_id and apply_variants:
                raise ValidationError(
                    _("You cannot use the 'Apply on Variant' functionality and simultaneously create a BoM for a specific variant."))
            for ptav in apply_variants:
                if ptav.product_tmpl_id != bom.product_tmpl_id:
                    raise ValidationError(_(
                        "The attribute value %(attribute)s set on product %(product)s does not match the BoM product %(bom_product)s.",
                        attribute=ptav.display_name,
                        product=ptav.product_tmpl_id.display_name,
                        bom_product=bom_line.parent_product_tmpl_id.display_name
                    ))
            for byproduct in bom.byproduct_ids:
                if bom.product_id:
                    same_product = bom.product_id == byproduct.product_id
                else:
                    same_product = bom.product_tmpl_id == byproduct.product_id.product_tmpl_id
                if same_product:
                    raise ValidationError(_("By-product %s should not be the same as BoM product.") % bom.display_name)
                if byproduct.cost_share < 0:
                    raise ValidationError(_("By-products cost shares must be positive."))
            # if sum(bom.byproduct_ids.mapped('cost_share')) > 100:
            #     raise ValidationError(_("The total cost share for a BoM's by-products cannot exceed 100."))


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    cost_share = fields.Float("Cost Share")

    def _get_cost_share(self):
        self.ensure_one()
        if self.cost_share:
            return self.cost_share
        bom = self.bom_id
        bom_lines_without_cost_share = bom.bom_line_ids.filtered(lambda bl: not bl.cost_share)
        return bom_lines_without_cost_share

