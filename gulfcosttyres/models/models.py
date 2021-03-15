# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GulfCostTyres(models.Model):
    _inherit = 'product.template'

    dot = fields.Char(string="DOT")




