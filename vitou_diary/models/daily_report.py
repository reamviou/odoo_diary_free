
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
from odoo.exceptions import ValidationError, UserError
import os






class VitouDiaryDailyReport(models.Model):
     _name = 'vitoudiary.dailyreport'
     #_inherit = ['mail.thread']
     _description = 'Daily Report'
     # _sql_constraints = [
     #      ('name_unique', 'unique(name)', "Provider is duplicated!"),
     # ]


     # reference = fields.Char(string="Reference", default='New')
     name = fields.Text(string="Report Title", required =True)
     #note = fields.Text(string="Note")
     date = fields.Date(string="Date", default =  fields.Date.today())
     #image = fields.Image(string="Image", help="Select image here", max_width=200, max_height=200)

     report_line_ids = fields.One2many(comodel_name="vitoudiary.dailyreportline",
                                          inverse_name="report_id",
                                          string='Report ID Line',
                                          help="Report ID Line")

     state = fields.Selection(
          string="State",
          selection=[
               ('posted', 'Posted'),
               ('done', 'Done'),
          ], default="posted", required=True
     )
     type= fields.Selection(
          string="Type",
          selection=[
               ('daily','Daily'),
               ('monthly','Monthly'),
               ('yearly','Yearly')
                     ],
          default='daily', required=True
     )

     employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", store=True, required=True,
                                domain=lambda self: [('user_id', '=', self.env.user.id)])
     employee_name = fields.Char(related='employee_id.name', string='Employee Name',
                                 compute='_compute_employee_id')  # fields.Many2one(related="employee_id.name", string="Employee Name")

     department_id = fields.Many2one(related="employee_id.department_id", string="Department", store=True)

     job_id = fields.Many2one(related="employee_id.job_id", string="Position", store=True)
     company_id = fields.Many2one(related='employee_id.company_id', string='Company ID',  store=True)


     #cancel
     canceled_uid = fields.Char(string="Cancel By")
     canceled_date = fields.Datetime(string="Canceled Date", default=None)
     #done
     done_uid = fields.Char(string="Done By")
     done_date = fields.Datetime(string="Done Date", default=None)


     # @api.model_create_multi
     # def create(self, vals_list):
     #      #print("reference==",vals_list)
     #      # for vals in vals_list:
     #      #      if not vals.get('reference') or vals['reference'] == 'New':
     #      #           vals['reference'] = self.env['ir.sequence'].next_by_code('vitoudiary.diary')
     #      return super().create(vals_list)



     @api.onchange('date')
     def _compute_employee_id(self):
          for rec in self:
               user_id = self.env.user.id
               #print(user_id)
               record = self.env['hr.employee'].search([('user_id', '=', user_id)])
               #print('==>',record[0].id)

               if len(record)>0:
                    rec.employee_id = record[0].id
                    rec.employee_name = record[0].name
                   #rec.department_name = record[0].department_id.name
                    #rec.department_id = record[0].department_id.id
                    #rec.job_id = record[0].job_id.name
                    #rec.company_id = record[0].company_id.name

               else:
                    rec.employee_id = None
                    rec.employee_name = ''
                    # rec.department_name = ''
                    # rec.department_id = None
                    # rec.job_id = None
                    # rec.company_id = None

     # def _compute_priority(self):
     #      for rec in self:
     #
     #           record = self.env['vitoudiary.priority'].search([('id', '=', rec.priority_id.id)])
     #           #print('==>',record.value)
     #           if record:
     #                rec.priority_value = record.value
     #                rec.priorityvalue = record.value
     #
     #
     #           else:
     #                rec.priority_value = 0
     #                rec.priorityvalue = 0


     def action_done(self):
          for rec in self:
               if rec.state == "posted":
                    user_id = self.env.user.id
                    #print('==', user_id,'=', rec.create_uid)
                    if rec.create_uid.id != user_id:
                         return self.env['vitoudiary.func'].myinfo('Oop! It is not yours! Cannot Apply done','warning')
                    else:
                         rec.state = "done"
                         rec.done_uid = self.env.user.login
                         rec.done_date = fields.Date.today()
               else:
                    raise ValidationError(_("Invalid function!"))

     def action_canceled(self):
          for rec in self:
               if rec.state == "done":
                    rec.state = "posted"
                    rec.canceled_uid = self.env.user.login
                    rec.canceled_date = fields.Date.today()
               else:
                    raise ValidationError(_("Invalid function!"))



     # def open_folder(self):
     #      path = self.folder
     #      if path:
     #           try:
     #                os.startfile(path)
     #           except Exception as e:
     #                raise Warning('An error occurred while opening the folder: {}'.format(e))
     #      else:
     #           raise Warning('No folder path specified.')

