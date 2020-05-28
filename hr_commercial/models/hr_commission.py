# -*- coding: utf-8 -*-
import time
from datetime import datetime
from odoo import fields, models, api, _
from odoo.exceptions import except_orm
from odoo import exceptions

class HrCommissionPayment(models.Model):
    _name = "hr.commission"

    name = fields.Char(string='Nom', readonly=True, default=lambda self: 'Com/')
    employee_id = fields.Many2one('hr.employee', string='Employé', required=True)
    date = fields.Date(string='Date', required=True, default=lambda self: fields.Date.today())
    commission_ca = fields.Float(string='Commission sur CA du mois', required=False)
    commission_vd = fields.Float(string='Commission Vente Directe du mois', required=False)
    currency_id = fields.Many2one('res.currency', string='Devise', required=True,
                                  default=lambda self: self.env.user.company_id.currency_id)
    company_id = fields.Many2one('res.company', string='Entreprise', required=True,
                                 default=lambda self: self.env.user.company_id)
    department = fields.Many2one('hr.department', string='Département')
    employee_contract_id = fields.Many2one('hr.contract', string='Contrat')


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].get('hr.commission.seq') or ' '
        res_id = super(HrCommissionPayment, self).create(vals)
        return res_id

    @api.onchange('employee_id')
    def onchange_employee_id(self):
        department_id = self.employee_id.department_id.id
        domain = [('employee_id', '=', self.employee_id.id)]
        return {'value': {'department': department_id}, 'domain': {
            'employee_contract_id': domain,
        }}

    @api.onchange('company_id')
    def onchange_company_id(self):
        company = self.company_id
        domain = [('company_id.id', '=', company.id)]
        result = {
            'domain': {
                'journal': domain,
            },

        }
        return result
