# © 2024 Forgar (<https://fogardosantiso.es/>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class AccountMoveLive(models.Model):
    _inherit = "account.move.line"

    date_deadline = fields.Datetime("mrp.production")
