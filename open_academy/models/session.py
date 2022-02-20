# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'Session module description'

    name = fields.Char(string='Session')
    startdate = fields.Char(string='Start-date')
    duration = fields.Integer(string='Duration')
    seats = fields.Integer(string='Number of seats')
    instructor = fields.Many2one('res.partner', ondelete='set null')
    course = fields.Many2one('open_academy.course', ondelete='set null')
    attendees = fields.Many2many('res.partner')