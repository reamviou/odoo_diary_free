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

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

#open file dialog
import tkinter as tk
from tkinter import filedialog
import os





class VitouDiaryFunc(models.Model):
     _name = 'vitoudiary.func'
     _description = "Function"



     #report leading zero
     def leading_zero(self, value,digit):
          f ="{:0"+ digit +"d}"
          #print(f)
          # return "{:09d}".format(value)
          return f.format(value)
     def reload(self):
          return {
               'type': 'ir.actions.client',
               'tag': 'reload',
          }

     def myinfo(self, message, infotype):
          # /'success', 'info', 'warning'
          return {
               'type': 'ir.actions.client',
               'tag': 'display_notification',
               'params': {
                    'message': message,
                    'type': infotype,
                    'sticky': False
               }
          }

     def get_staff(self, user_id):
          data = self.env['hr.employee'].search([('user_id', '=', user_id)])
          staffname = ""
          if len(data) > 0:
               staffname = data.name
          return staffname

     def open_new_form(self, name, model, folder_formname):
          return {

               'name': name,  # 'Checkin',

               'view_mode': 'form',

               'res_model': model,  # 'room.booking',

               'view_id': self.env.ref(folder_formname).id,  # vitou_hotel_management.room_booking_view_form

               # 'context': {'default_name': self.name.id},

               'target': 'new',

               'type': 'ir.actions.act_window',

          }

     def open_new_form(self, name, model, folder_formname, view_mode='form',target='new'):
          return {

               'name': name,  # 'Checkin',

               'view_mode': view_mode,

               'res_model': model,  # 'room.booking',

               'view_id': self.env.ref(folder_formname).id,  # vitou_hotel_management.room_booking_view_form

               # 'context': {'default_name': self.name.id},

               'target': target,

               'type': 'ir.actions.act_window',

          }



     def open_form_by_id(self, title, model, folder_formname, id, target, view_mode='form'):
          # return self.env['vitouhotel.func'].open_form_by_id( 'Clean Request', 'cleaning.request',
          # 'vitou_hotel_management.cleaning_request_view_form', room_clean.id, 'current')
          return {
               'name': title,  # 'Checkin',
               'view_mode': view_mode, #'form',
               'res_model': model,  # 'room.booking',
               'view_id': self.env.ref(folder_formname).id,  # vitou_hotel_management.room_booking_view_form
               'res_id': id,  # for get by id
               # 'res_id': ids.id,
               # 'context': {'default_cleaning_type': 'room', 'default_room_id': rec.id}, #for default value
               'target': target,  # 'new','current','inline','fullscreen'
               'type': 'ir.actions.act_window',

          }

     def open_form_with_default(self, title, model, folder_formname, context, target, view_mode='form'):
          # return self.env['vitouhotel.func'].open_form_with_default( 'Clean Request', 'cleaning.request',
          # 'vitou_hotel_management.cleaning_request_view_form', {'default_cleaning_type': 'room', 'default_room_id': rec.id}, 'current' )

          return {
               'name': title,  # 'Checkin',
               'view_mode': view_mode,#'form',
               'res_model': model,  # 'room.booking',
               'view_id': self.env.ref(folder_formname).id,  # vitou_hotel_management.room_booking_view_form
               # 'res_id': id,  # for get by id
               # 'res_id': ids.id,
               'context': context,
               # 'context': {'default_cleaning_type': 'room', 'default_room_id': rec.id}, #for default value
               'target': target,  # 'new','current','inline','fullscreen'
               'type': 'ir.actions.act_window',

          }

     def get_total_payout(self, operationday_id):
          # total payout
          #operationday_id = operationday_id.id

          payout = self.env['vitouslot.dailypayout'].search(
               [('operationday_id', '=', operationday_id), ('state', '=', 'approved')])
          t_payout = 0
          if len(payout) > 0:
               t_payout = sum(payout.mapped('totalamount'))
          return t_payout
     def get_total_slip(self, operationday_id, state):
          #operationday_id = operationday_id.id
          r = self.env['vitouslot.dailypayout'].search(
               [('operationday_id', '=', operationday_id), ('state', '=', state)])
          return len(r)

     def get_total_slip_approve_close_day(self, operationday_id):
          r = self.env['vitouslot.dailypayout'].search(
               [('operationday_id', '=', operationday_id), ('state', '=', 'approved'), ('isclosedday', '=', True)])
          return len(r)

     def get_total_slip_approve_close_shift(self, operationday_id):
          r = self.env['vitouslot.dailypayout'].search(
               [('operationday_id', '=', operationday_id), ('state', '=', 'approved'), ('isclosedshift', '=', True)])
          return len(r)

     def get_total_slip_post(self, operationday_id):
          r = self.env['vitouslot.dailypayout'].search(
               [('operationday_id', '=', operationday_id), ('state', '=', 'posted')])
          return len(r)

     def get_total_payout_yours(self, operationday_id, uesrlogin):
          #uesrlogin = self.env.user.id
          #operationday_id = operationday_id.id
          payout_yours = self.env['vitouslot.dailypayout'].search(
               [('operationday_id', '=', operationday_id), ('state', '=', 'approved'),
                ('approved_uid', '=', uesrlogin)])
          t_payout_yours = 0
          if len(payout_yours) > 0:
               t_payout_yours = sum(payout_yours.mapped('total_payout'))
          return t_payout_yours

     def get_checkin_shift(self, userid):
          #userid=self.env.user.id
          shift = self.env['vitouslot.checkin'].search(
               [('state', '=', 'checkin'), ('checkin_uid', '=', userid)])
          #print('==>', shift)
          if len(shift) > 0:
               return shift.shift_name
          else:
               return None
               #return self.env['vitouslot.func'].myinfo("You're not yet check in!", 'warning')


     def open_file_dialog(self):
          root = tk.Tk()
          toplevel = tk.Toplevel()

          # file_path = filedialog.askopenfilename(parent=tk.Toplevel(), initialdir="/", title="Select a File",
          #                                        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
          file_path = filedialog.askopenfilename(parent=toplevel,initialdir="/", title="Select a File",
                                                 filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
          root.destroy()
          root.mainloop()
          return file_path

     def open_file(self, path):
          #path = self.folder
          if path:
               try:
                    os.startfile(path)
               except Exception as e:
                    path_new = path.replace("/","\\")
                    os.startfile(path_new)
                    #os.open(path,os.O_RDONLY,0o666)
                   # raise Warning('An error occurred while opening the folder: {}'.format(e))
          else:
               raise Warning('No folder path specified.')

     def open_folder(self, path):

          #print('=', self.department_id.name)
          #path = self.folder
          # dsplit = path.partition('\')
          dsplit = os.path.split(path)
          #print(self.department_id)
          folder_path =  dsplit[0]
          #print(folder_path)

          if folder_path:
               try:
                    os.startfile(folder_path)
               except Exception as e:
                    path_new = folder_path.replace('/','\\')
                    os.startfile(path_new)
                    #raise Warning('An error occurred while opening the folder: {}'.format(e))
          else:
               raise Warning('No folder path specified.')


