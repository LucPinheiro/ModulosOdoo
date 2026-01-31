# © 2024 Forgar (<https://fogardosantiso.es/>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class StockMove(models.Model):
    _name = "food.allergens"

    name = fields.Char()
