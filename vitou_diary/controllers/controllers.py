# -*- coding: utf-8 -*-
from werkzeug.exceptions import BadRequest

from odoo import http, api
from odoo.http import request, Response
from odoo.http import werkzeug
import json
class CtrItControl(http.Controller):
    _inherit = 'ir.http'
    _inherit ='res.users.apikeys'
    _inherit ='itcontrol.approval'

