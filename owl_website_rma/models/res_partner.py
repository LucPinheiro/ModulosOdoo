from odoo import models,api, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    


    @api.model
    def get_client_info(self):
        user = self.env.user.partner_id
        return {
            'name': user.name,
            'shipping_address': user,
            'billing_address': user,  
            'source_document': 'Portal'  
        }
