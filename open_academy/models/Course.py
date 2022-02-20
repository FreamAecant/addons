# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course description'

    name = fields.Char(string='Course')
    title = fields.Char(string='Title')
    description = fields.Text(string='Description')
    responsible = fields.Many2one('res.users', ondelete='set null')
    sessions = fields.One2many('open_academy.session', 'course')


    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
