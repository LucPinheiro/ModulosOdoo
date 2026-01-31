from odoo import api, fields, models
from odoo.exceptions import ValidationError

class TmsVehicle(models.Model):
    _name = "tms.vehicle"
    _description = "TMS Vehicle"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    name = fields.Char(required=True, tracking=True)
    license_plate = fields.Char(tracking=True)
    model = fields.Char(tracking=True)
    brand = fields.Char(tracking=True)
    driver_id = fields.Many2one("res.partner", string="Conductor", domain=[("is_company","=",False)], tracking=True)
    odometer = fields.Float(string="Odómetro (km)", tracking=True)

    # GPS simple
    latitude = fields.Float(tracking=True)
    longitude = fields.Float(tracking=True)
    last_position_date = fields.Datetime(tracking=True)

    active = fields.Boolean(default=True)

    @api.constrains("latitude","longitude")
    def _check_lat_lon(self):
        for rec in self:
            if rec.latitude and (rec.latitude < -90 or rec.latitude > 90):
                raise ValidationError("Latitud inválida.")
            if rec.longitude and (rec.longitude < -180 or rec.longitude > 180):
                raise ValidationError("Longitud inválida.")
