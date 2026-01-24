# © 2024 Forgar (<https://fogardosantiso.es/>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = "mrp.production"


    food_allergen_ids = fields.Many2many("food.allergens",  compute='_compute_food_allergens')
    allergens = fields.Many2one("product.template")


    @api.depends('move_raw_ids.food_allergen_ids')
    def _compute_food_allergens(self):
        for production in self:
            allergens = production.move_raw_ids.mapped('food_allergen_ids')
            production.food_allergen_ids = allergens
