# -*- coding: utf-8 -*-
###################################################################################
#    A part of Open HRMS Project <https://www.openhrms.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).
#    Author: Anusha P P (<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
{
    'name': 'Commission Commerciale Paie Maroc',
    'version': '12.0.1.0.0',
    'summary': 'Commission Commercial in HR',
    'description': """
        Helps you to manage Commission commercial Salary Request of your company's staff.
        """,
    'category': 'Generic Modules/Human Resources',
    'author': "PINTFORGE",
    'company': 'PINTFORGE',
    'maintainer': 'PINTFORGE',
    'website': "https://www.pintforge.com",
    'depends': [
        'hr_payroll', 'hr', 'account', 'hr_contract', 'ohrms_loan',
    ],
    'data': [
    'views/hr_commission_view.xml',
    'security/ir.model.access.csv',
    'data/salary_rule_commission.xml',
    ],
    'demo': [],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
