# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models


class SalaryRuleInput(models.Model):
    _inherit = 'hr.payslip'

    def get_inputs(self, contract_ids, date_from, date_to):
        """This Compute the other inputs to employee payslip.
                           """
        res = super(SalaryRuleInput, self).get_inputs(contract_ids, date_from, date_to)
        contract_obj = self.env['hr.contract']
        emp_id = contract_obj.browse(contract_ids[0].id).employee_id
        com_salary = self.env['hr.commission'].search([('employee_id', '=', emp_id.id)])
        for com_obj in com_salary:
            current_date = datetime.strptime(str(date_from), '%Y-%m-%d').date().month
            date = com_obj.date
            existing_date = datetime.strptime(str(date), '%Y-%m-%d').date().month
            if current_date == existing_date:
                amount_ca = com_obj.commission_ca
                amount_vd = com_obj.commission_vd
                for result in res:
                    if amount_ca != 0 and result.get('code') == 'COMCA':
                        result['amount'] = amount_ca
                    if amount_vd != 0 and result.get('code') == 'COMVD':
                        result['amount'] = amount_vd
        return res
