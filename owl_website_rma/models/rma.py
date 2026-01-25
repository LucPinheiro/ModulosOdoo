

from odoo import models, fields


class Rma(models.Model):
    _inherit = "rma"

    product_id = fields.Many2one('product.product', string="Producto")
    operation_id = fields.Many2one('rma.operation', string="Operación")
    description = fields.Text(string="Descripción")
    product_name = fields.Char(string="Product Name")
    product_category = fields.Char(string="Product Category")
    client = fields.Char('Cliente')
    shipping_address = fields.Text('Dirección de Envío')
    billing_address = fields.Text('Dirección de Facturación')
    origin = fields.Char('Origen de la solicitud')



    def website_form_input_filter(self, request, values):
        values.update(
            team_id=values.get("team_id") or request.website.rma_default_team_id.id,
            user_id=values.get("user_id") or request.website.rma_default_user_id.id,
            partner_id=values.get("partner_id") or request.env.user.partner_id.id,
            origin="Website form",
        )
        return values

    order_id = fields.Many2one("sale.order",
        string="Sale Order",)
