
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

#open file dialog
import tkinter as tk
from tkinter import filedialog


class VitouDiaryDailyReport(models.Model):
     _name = 'vitoudiary.dailyreportline'
     _inherit = ['mail.thread']
     _description = 'Daily Report Line'
     # _sql_constraints = [
     #      ('name_unique', 'unique(name)', "Provider is duplicated!"),
     # ]


     # reference = fields.Char(string="Reference", default='New')
     report_id = fields.Many2one("vitoudiary.dailyreport", string="Report ID", required=True,
                                  help="Report ID",
                                  ondelete="cascade")
     name = fields.Text(string="Note", required =True, tracking=True)
     date = fields.Date(string="Date", default =  fields.Date.today())
     #image = fields.Image(string="Image", help="Select image here", max_width=200, max_height=200)


     # domain = lambda self: [('department_id', '=', self.department_id)]
     reporttype_id = fields.Many2one(comodel_name="vitoudiary.reporttype", string="Report Type", store=True, required=True)
     departmentreport_id = fields.Many2one(related="reporttype_id.department_id", string="Department ID", store=True)

     state = fields.Selection(related='report_id.state',
                             string="State",
                             help="Sate",
                             copy=False)


     note = fields.Text(string="Note")
     folder = fields.Text(string="File Name and Path")


     employee_id = fields.Many2one(related='report_id.employee_id', string="Employee", store=True,copy=True)
     department_id = fields.Many2one(related="employee_id.department_id", string="Department", store=True )
     job_id = fields.Many2one(related="employee_id.job_id", string="Position", store=True)
     company_id = fields.Many2one(related='employee_id.company_id', string='Company', store=True)




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

     # def action_open_file_dialog(self):
     #      file_path = filedialog.askopenfilename(title="Select a File",
     #                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
     #      if file_path:
     #           print(file_path)
     #           # selected_file_label.config(text=f"Selected File: {file_path}")
     #           # process_file(file_path)

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

