# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Morocco Payroll',
    'category': 'Human  Resources',
    'depends': [
    "hr_payroll",
    ],
    'description': """
Moroccan Payroll Salary Rules.
==============================
-Configuration of hr_payroll for Morocco localization
    -All main contributions rules for Morocco payslip.

    """,
    'data': [
        'views/l10n_ma_hr_payroll_view.xml',
        #'data/l10n_ma_hr_payroll_data.xml',
     ],
    'depends': ['hr'],
}
