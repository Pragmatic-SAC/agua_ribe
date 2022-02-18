# -*- coding: utf-8 -*-
{
    'name': "Blueline Custom Invoice",

    'summary': """
        Custom Invoice Report For Mexican Accounting""",

    'description': """
        Blueline Custom Invoice Report For Mexican Accounting
    """,

    'author': "Kelvin Meza",
    'website': "http://www.pragmatic.com.pe",
    'category': 'Invoicing Management',
    'version': '0.1',

    'depends': ['l10n_mx_edi'],

    # always loaded
    'data': [
        'data/3.3/cfdi.xml',
        'data/data.xml',
        'views/account_tax.xml',
        'views/account_move.xml',
        'views/template.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'blueline_l10n_mx_custom_invoice/static/src/less/report.less',
        ],
    }
}
