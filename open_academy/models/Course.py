# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course description'

    name = fields.Char(string='Course')
    title = fields.Char(string='Title')
    description = fields.Text(string='Description')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
