# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2024-TODAY,
#    Author: REAM Vitou (reamvitou@yahoo.com)
#    Tel: +855 17 82 66 82

#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import datetime

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class VitouDiaryReportType(models.Model):
     _name = 'vitoudiary.reporttype'
     _inherit = ['mail.thread']
     _description = 'Report Type'
     _sql_constraints = [
          ('name_unique', 'unique(name)', "Report Type is duplicated!"),
     ]


     #reference = fields.Char(string="Reference", default='New')
     name = fields.Char(string="Report Type", required =True, tracking=True)
     department_id = fields.Many2one(comodel_name='hr.department', string="Department", store=True, required=True)
     #fields.Char(string="Department Report")




     # @api.model_create_multi
     # def create(self, vals_list):
     #      #print("reference==",vals_list)
     #      for vals in vals_list:
     #           if not vals.get('reference') or vals['reference'] == 'New':
     #                vals['reference'] = self.env['ir.sequence'].next_by_code('vitoudiary.diary')
     #      return super().create(vals_list)
     #
     #
     # def _compute_employee_id(self):
     #      for rec in self:
     #           user_id = rec.create_uid.id
     #           print(user_id)
     #           record = self.env['hr.employee'].search([('user_id', '=', user_id)])
     #           if record:
     #                rec.employee_id = record.id
     #                rec.employee_name = record.name
     #                rec.department_name = record.department_id.name
     #                rec.job_name = record.job_id.name
     #                rec.company_name = record.company_id.name
     #
     #           else:
     #                rec.employee_id = 0
     #                rec.employee_name = ''
     #                rec.department_name = ''
     #                rec.job_name = ''
     #                rec.company_name = ''
     #
     # def action_done(self):
     #      for rec in self:
     #           if rec.state == "posted":
     #                rec.state = "done"
     #                rec.done_uid = self.env.user.login
     #                rec.done_date = fields.Date.today()
     #           else:
     #                raise ValidationError(_("Invalid function!"))
     #
     #