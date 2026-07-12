# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from . import models
from . import report
from . import wizard


# KMEE PATCH (18.0): fix temporario ate upstream corrigir. Ver
# https://github.com/odoo/odoo/pull/273905 (commit que introduziu o bug,
# fechado sem merge visivel no GitHub - processo interno da Odoo SA).
# Remover este patch quando um sync futuro do OCB ja trouxer o fix.
def _configure_journals(env):
    # if we already have a coa installed, create journal and set property field
    for company in env['res.company'].search([('chart_template', '!=', False)], order="parent_path"):
        ChartTemplate = env['account.chart.template'].with_company(company)
        template_code = company.chart_template
        template_data = ChartTemplate._get_chart_template_data(template_code)['template_data']
        if 'property_stock_account_production_cost_id' in template_data:
            value = template_data['property_stock_account_production_cost_id']
            if not ChartTemplate.ref(value, raise_if_not_found=False):
                # chart_template is set but its accounts were never actually
                # loaded (e.g. a demo company created without a real CoA)
                continue
            data = {'property_stock_account_production_cost_id': value}
            ChartTemplate._post_load_data(template_code, company, data)
