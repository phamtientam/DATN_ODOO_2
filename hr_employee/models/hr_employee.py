from odoo import api, fields, models, tools, _

class HrEmployee(models.Model):
    _name = 'hr.employee'
    _description = 'HR Employee'
    _inherit = 'hr.employee'

    status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('waiting_approve', 'Waiting Approve'),
            ('approved', 'Approved'),
            ('terminated', 'Terminated'),
        ], string='Status', default='draft', readonly=True
    )
    # work_experiences_ids = fields.One2many('work.experiences', 'employee_id', string='Work Experiences')
    # role_name = fields.Char(related="work_experiences_ids.role_id.name")
    # level_name = fields.Char(related="work_experiences_ids.level_name")
    # job_name = fields.Char(related="work_experiences_ids.job_name")

    def action_submit(self):
        self.status = "waiting_approve"

    def action_approve(self):
        self.status = 'approved'

    def action_terminate(self):
        self.status = 'terminated'

    def action_set_to_draft(self):
        self.status = 'draft'
