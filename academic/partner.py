from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = "res.partner"

    is_instructur = fields.Boolean(string="Is Instructur")
