# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sessions = fields.Many2many('open_academy.session')