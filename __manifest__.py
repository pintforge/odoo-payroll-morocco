# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Morocco Payroll',
    'category': 'Human  Resources',
    'depends': [
    "hr_payroll",
    "report_xml",
    ],
    'description': """
Morocco Payroll Salary Rules.
==============================
-Configuration of hr_payroll for Morocco localization
    -All main contributions rules for Morocco payslip.

    """,
    'data': [
         '',
     ],
    'depends': ['hr', 'hr_contract', 'hr_employee_service', 'hr_employee_service_contract'],
}
