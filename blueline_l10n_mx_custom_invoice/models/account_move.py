# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_xml_values(self):
        return self.env['account.edi.format']._l10n_mx_edi_get_invoice_cfdi_values(self)

    def get_l10n_mx_edi_usage_label(self):
        Invoice = self.with_context({'lang': self.partner_id.lang})
        return 'prueba'

        # return Invoice.env['ir.translation']._get_source(None, ('selection',), self.partner_id.lang,
        #                                                  dict(self._fields['l10n_mx_edi_usage']._description_selection(
        #                                                      self.env)).get(self.l10n_mx_edi_usage)
        #                                                  )
