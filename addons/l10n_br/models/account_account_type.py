# -*- coding: utf-8 -*-
# Copyright 2017 KMEE INFORMATICA LTDA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from __future__ import division, print_function, unicode_literals
from odoo import api, fields, models, _


class AccountAccountType(models.Model):

    _inherit = 'account.account.type'

    is_redutor = fields.Boolean(
            string='Redutor?',
            compute='_compute_is_redutor',
            store=True,
        )

    @api.depends('name')
    def _compute_is_redutor(self):
        for account_type in self:
            if account_type.name and (
                        account_type.name.startswith('(-)') or
                        account_type.name.startswith('( - )')):
                account_type.redutor = True
            account_type.redutor = False
