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
