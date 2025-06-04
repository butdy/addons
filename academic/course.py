from odoo import api, fields, models, _
class Course(models.Model):
    _name ='academic.course'
    _description = 'Course'
    name = fields.Char('Name')
    description = fields.Text(string="Description", required=True)
    responsible_id = fields.Many2one(
        comodel_name = "res.users",
        string="responsible",
    )

    session_ids = fields.One2many(
        comodel_name="academic.session",
        inverse_name="course_id",
        string="Sessions",
        ondelete="cascade",
    )

    _sql_constraints = [
        ('check_name_unique','UNIQUE(name)','Nama Course harus unik'),
        ('check_name_desc','CHECK(name<>description)','Nama dan Description course tidak boleh sama')
    ]