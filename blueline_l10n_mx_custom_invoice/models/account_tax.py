# -*- coding: utf-8 -*-
from odoo import api, fields, models

_TAX_CODES = {'ISR': '001', 'IVA': '002', 'IEPS': '003'}


class AccountTax(models.Model):
    _inherit = 'account.tax'

    tax_code = fields.Selection([('001', 'ISR'), ('002', 'IVA'), ('003', 'IEPS')])
