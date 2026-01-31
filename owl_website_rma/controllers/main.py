from odoo import http
from odoo.http import request

class Main(http.Controller):

    @http.route('/custom_website_rma', type='http', auth='public', website=True, csrf=False, methods=['GET', 'POST'])
    def owl_custom(self, **post):
        if request.httprequest.method == 'GET':
            # Renderizar el formulario cuando se accede por GET
            return request.render('owl_website_rma.custom_page_website_rma')

        if request.httprequest.method == 'POST':
            # Recibir los valores del formulario
            product_id = post.get('product_id')
            operation_id = post.get('operation_id')
            description = post.get('description')

            # Validar que los campos producto, operación y descripción están presentes
            if not (product_id and operation_id and description):
                return request.render('owl_website_rma.rma_error_page', {
                    'error': 'Producto, operación y descripción son obligatorios. Por favor, complete estos campos correctamente.'
                })

            try:
                # Crear un registro en el modelo RMA
                rma_order = request.env['rma'].sudo().create({
                    'product_id': int(product_id),
                    'operation_id': int(operation_id),
                    'description': description,
                    'origin': 'Portal',
                    'partner_id': request.env.user.partner_id.id,  # Relacionar con el usuario actual
                })

                # Redirigir o mostrar una página de agradecimiento si se crea correctamente
                return request.render('owl_website_rma.rma_thanks_page', {
                    'rma_order': rma_order
                })

            except Exception as e:
                # Manejo de errores
                return request.render('owl_website_rma.rma_error_page', {
                    'error': f'Ocurrió un error al procesar la solicitud: {str(e)}'
                })
            
    @http.route('/rma_thanks_page', type='http', auth='public', website=True)
    def rma_thanks_page(self, **kwargs):
        return request.render('owl_website_rma.rma_thanks_page')

