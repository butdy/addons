from odoo import api,fields,models, _

class Instructor(models.Model):
        _name ='academic.instructor'
        _description = 'Instructor'
        name = fields.Text(string="Name", required=True)

        partner_id = fields.Many2one('res.partner', string='Related Partner')
