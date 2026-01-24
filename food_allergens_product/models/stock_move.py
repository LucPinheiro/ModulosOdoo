# © 2024 Forgar (<https://fogardosantiso.es/>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class StockMove(models.Model):
    _inherit = "stock.move"
    
    food_allergen_ids = fields.Many2many( "food.allergens", related='product_id.food_allergen_ids')
