# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Brazilian - Accounting',
    'category': 'Localization',
    'description': """Base da contabilidade brasileira

Estrtura dos relatórios contábeis

- DRE
- Balanço Patrimonial

================================
""",
    'author': 'Odoo Brasil',
    'website': 'http://www.odoobrasil.org.br',
    'depends': ['account'],
    'data': [
        'data/account_account_type_dre_data.xml',
        'data/account_account_type_balanco_data.xml',
        'data/account_financial_report_dre_data.xml',
        'data/account_financial_report_balanco_data.xml',
    ],
}
