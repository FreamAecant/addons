# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'open_academy.session'
    _description = 'Session module description'

    name = fields.Char(string='Session')
    startdate = fields.Char(string='Start-date')
    duration = fields.Integer(string='Duration')
    seats = fields.Integer(string='Number of seats')