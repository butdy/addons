from odoo import api,fields,models, _

class Attendee(models.Model):
        _name ='academic.attendee'
        _description = 'Attende'
        name = fields.Char(string='Name')

        session_id = fields.Many2one(comodel_name="academic.session",string="Sessions")
        partner_id = fields.Many2one(comodel_name="res.partner",string="Attendee")

        @api.onchange('partner_id')
        def _onchange_seats(self):
            self.name = self.partner_id.id
            
      ##### AWAL TAMBAHAN untuk otomatis menambahkan name pada list attendee di session  ########
        @api.model
        def create(self, vals):
            if vals.get('partner_id') and not vals.get('name'):
               partner = self.env['res.partner'].browse(vals['partner_id'])
               vals['name'] = partner.name
            return super().create(vals)
      ##### END TAMBAHAN ########

        _sql_constraints = [
              ('partner_session_unik','UNIQUE(session_id,partner_id)','Tidak boleh Multiple Attende')
        ]
        course_id = fields.Many2one(
              comodel_name="academic.course",
              string="Course",
              related="session_id.course_id", 
              store=True)