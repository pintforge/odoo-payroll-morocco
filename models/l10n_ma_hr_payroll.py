# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError

class ResCompany(models.Model):
    _inherit = 'res.company'

    affil_cnss = fields.Char(string="N° Affiliation CNSS")
    affil_cimr = fields.Char(string="N° Affiliation CIMR")
    taux_cimr_salar = fields.Char(string="Taux CIMR Salariale")
    taux_cimr_part = fields.Char(string="Taux CIMR Patronale")
    ice = fields.Char(string="I.C.E")
    patente = fields.Char(string="Patente N°")
    tp = fields.Char(string="Taxe Professionnelle")
    code_commune = fields.Char(string="Code Commune pour IR")
    bank = fields.One2many('res.partner.bank', 'bank_id')
    count_total = fields.Char(string="Nombre d'employés",)
    count_permanent = fields.Char(string="Nombre d'employés Permanents",)
    count_occas = fields.Char(string="Nombre d'employés Occasionnelles",)
    count_stag = fields.Char(string="Nombre de stagiaires",)

class HrContract(models.Model):
    """
    Employee contract allows to add different values in fields.
    Fields are used in salary rule computation.
    """
    _inherit = 'hr.contract'

    indemnite_transport = fields.Float(string='Indémnité de Transport', digits=dp.get_precision('payroll'), help='Indémnité de Transport')
    prime_panier = fields.Float(string='Prime de Panier', digits=dp.get_precision('payroll'),
    help='Prime de Panier')
    prime_fonction = fields.Float(string='Prime de Fonction', digits=dp.get_precision('payroll'),
    help='Prime de Fonction')
    indemnite_representation = fields.Float(string='Indémnité de Représentation', digits=dp.get_precision('payroll'),
    help='Indémnité de Représentation')
    indemnite_voiture = fields.Float(string='Indémnité de Voiture', digits=dp.get_precision('payroll'),
    help='Indémnité de Voiture')
    
 class ResBank(models.Model):
    _inherit = 'res.bank'

    bank_virement = fields.Many2one('res.partner.bank', string='Banque de réception')
    bank_virement_id = fields.Many2one('res.bank', string='Banque de réception', related='bank_virement.bank_id')
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
        states={'draft': [('readonly', False)]}, default=lambda self: self.env.user.company_id)
