# -*- coding: utf-8 -*-
###################################################################################
#    A part of Open HRMS Project <https://www.openhrms.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).
#    Author: Treesa Maria Jude  (<https://www.cybrosys.com>)
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
    'name': 'Open HRMS Employee Logement',
    'version': '12.0.1.0.0',
    'summary': """Employee Interet Logement Principal pour la Paie Maroc.""",
    'description': """Gestion des intérêts Logement Principal pour la Paie Maroc.""",
    'category': 'Generic Modules/Human Resources',
    'author': 'WAHBI ACHRAF',
    'maintainer': 'PINTFORGE',
    'company': 'PINTFORGE',
    'website': 'https://www.pintforge.com',
    'depends': [
                'base', 'hr', 'hr_payroll', 'hr_employee_updation', 'l10n_ma_hr_payroll'
                ],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_logement_security.xml',
        'views/employee_logement_view.xml',
        'views/logement_salary_stucture.xml',
              ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
