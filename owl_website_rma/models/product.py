from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = 'product.product'

    category_breadcrumb = fields.Json(compute='_compute_category_breadcrumb', store=False)

    def _compute_category_breadcrumb(self):
        for product in self:
            breadcrumb = []
            current = product.public_categ_ids[:1]  # solo la primera categoría
            while current:
                breadcrumb.insert(0, {
                    'id': current.id,
                    'name': current.name,
                    'slug': '/shop/category/%s' % current.id,
                })
                current = current.parent_id
            product.category_breadcrumb = breadcrumb

