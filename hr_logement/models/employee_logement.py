# -*- coding: utf-8 -*-
###################################################################################
#    A part of OpenHRMS Project <https://www.openhrms.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).
#    Author: Treesa Maria Jude (<https://www.cybrosys.com>)
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

import time
from datetime import datetime,date
from dateutil import relativedelta
from odoo import models, fields, api, _


class EmployeeLogement(models.Model):
    _name = 'hr.logement'
    _description = 'HR Logement'
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    #logement_id = fields.Many2one('insurance.policy', string='Policy', required=True)
    amount = fields.Float(string='Montant Interêt Log', required=True)
    #sum_insured = fields.Float(string="Sum Insured", required=True)
    #policy_coverage = fields.Selection([('monthly', 'Monthly'), ('yearly', 'Yearly')],
    #                                   required=True, default='monthly',
    #                                   string='Policy Coverage',)
    date_from = fields.Date(string='Date From',
                            default=time.strftime('%Y-%m-%d'), readonly=False)
    date_to = fields.Date(string='Date To',   readonly=False,
                          default=str(datetime.now() + relativedelta.relativedelta(months=+1, day=1, days=-1))[:10])
    #state = fields.Selection([('active', 'Active'),
    #                          ('expired', 'Expired'), ],
    #                         default='active', string="State",compute='get_status')
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.user.company_id)


class HrLogement(models.Model):
    _inherit = 'hr.employee'

    #insurance_percentage = fields.Float(string="Company Percentage ")
    #deduced_amount_per_month = fields.Float(string="Salary deduced per month", compute="get_deduced_amount")
    #deduced_amount_per_year = fields.Float(string="Salary deduced per year", compute="get_deduced_amount")
    logement = fields.One2many('hr.logement', 'employee_id', string="Interêt Logement Principal")



class LogementRuleInput(models.Model):
    _inherit = 'hr.payslip'

    def get_inputs(self, contract_ids, date_from, date_to):
        """This Compute the other inputs to employee payslip.
                           """
        res = super(LogementRuleInput, self).get_inputs(contract_ids, date_from, date_to)
        contract_obj = self.env['hr.contract']
        emp_id = contract_obj.browse(contract_ids[0].id).employee_id
        log_salary = self.env['hr.logement'].search([('employee_id', '=', emp_id.id)])
        for log_obj in log_salary:
            current_date = date_from
            date = log_obj.date_from
            if current_date == date:
                amount = log_obj.amount
                for result in res:
                    if amount != 0 and result.get('code') == 'LOG':
                        result['amount'] = amount
        return res
