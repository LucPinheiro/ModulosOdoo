# © 2024 Forgar (<https://fogardosantiso.es/>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    food_allergen_ids = fields.Many2many("food.allergens")
    product_id = fields.Many2one("mrp.production", string="Production")
    date_deadline = fields.Datetime("mrp.production")
    state = fields.Char(string='State')
    move_finished_ids = fields.Many2one('stock.move')