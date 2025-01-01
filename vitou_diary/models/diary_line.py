
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
import  os


class VitouDiaryTask(models.Model):
     _name = 'vitoudiary.diaryline'
     _inherit = ['mail.thread']
     _description = 'Diary Line'
     # _sql_constraints = [
     #      ('name_unique', 'unique(name)', "Provider is duplicated!"),
     # ]


     # reference = fields.Char(string="Reference", default='New')
     diary_id = fields.Many2one("vitoudiary.diary", string="Diary ID", required=True,
                                 help="Diary ID",
                                 ondelete="cascade")
     name = fields.Text(string="Title", required =True, tracking=True)
     date = fields.Date(string="Date", default =  fields.Date.today())
     #image = fields.Image(string="Image", help="Select image here", max_width=200, max_height=200)

     state = fields.Selection(related='diary_id.state',
                              string="State",
                              help="Sate",
                              copy=False)

     status_id = fields.Many2one(comodel_name="vitoudiary.status", string="Status", store=True)
     priority_id = fields.Many2one(comodel_name="vitoudiary.priority", string="Priority", store=True, tracking=True)
     priority_value = fields.Float(related='priority_id.value', string="Priority Value", store=True)
     Assignedby_id = fields.Many2one(comodel_name="hr.employee", string="Assinged By",
                                     store=True)  # fields.Char(string="Assigned By")

     note = fields.Text(string="Note")
     folder = fields.Text(string="File Name and Path")

     employee_id = fields.Many2one(related='diary_id.employee_id', string="Employee", store=True, copy=True)
     department_id = fields.Many2one(related="employee_id.department_id", string="Department", store=True)
     job_id = fields.Many2one(related="employee_id.job_id", string="Position", store=True)
     company_id = fields.Many2one(related='employee_id.company_id', string='Company', store=True)

     #cancel
     canceled_uid = fields.Char(string="Cancel By")
     canceled_date = fields.Datetime(string="Canceled Date", default=None)
     #done
     done_uid = fields.Char(string="Done By")
     done_date = fields.Datetime(string="Done Date", default=None)


     def action_open_file_dialog(self):
          file_get = self.env['vitoudiary.func'].open_file_dialog()
          if file_get:
               self.folder = file_get

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

     def open_file(self):
          self.env['vitoudiary.func'].open_file(self.folder)
     def open_folder(self):
          self.env['vitoudiary.func'].open_folder(self.folder)
