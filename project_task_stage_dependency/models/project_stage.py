from odoo import fields, models, _ 


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    previous_stage_ids = fields.Many2many(
        comodel_name='project.task.type',
        relation="previous_stage_ids_allowed",
        column1="stage_id",
        column2="previous_stage_id",
        string='Previous Stages',
        help="Stages the task can be moved to, leave empty in case you don't want validation"
    )
    next_stage_ids = fields.Many2many(
        comodel_name='project.task.type',
        relation="next_stage_ids_allowed",
        column1="stage_id",
        column2="next_stage_id",
        string='Next Stages',
        help="Stages the task can be moved to, leave empty in case you don't want validation"
    )
