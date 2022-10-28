from odoo import models, _ 
from odoo.exceptions import ValidationError


class Task(models.Model):
    _inherit = "project.task"

    def write(self, vals):
        if 'stage_id' in vals:

            stage_id = self.env['project.task.type'].browse(vals.get('stage_id'))
            old_stage_id = self.stage_id
            
            if stage_id.sequence < old_stage_id.sequence and old_stage_id.previous_stage_ids:
                if stage_id.id not in old_stage_id.previous_stage_ids.ids:
                    message = _("The task cannot be moved to the %s stage, the allowed ones are the following: %s" %
                                (stage_id.name, old_stage_id.previous_stage_ids.mapped("name")))
                    raise ValidationError(message)

            if stage_id.sequence > old_stage_id.sequence and old_stage_id.next_stage_ids:
                if stage_id.id not in old_stage_id.next_stage_ids.ids:
                    message = _("The task cannot be moved to the %s stage, the allowed ones are the following: %s" %
                                (stage_id.name, old_stage_id.next_stage_ids.mapped("name")))
                    raise ValidationError(message)

        super().write(vals)
