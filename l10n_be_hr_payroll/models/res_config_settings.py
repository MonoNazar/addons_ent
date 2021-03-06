# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_commission_on_target = fields.Float(string="Commission on Target", default_model="hr.contract")
    default_fuel_card = fields.Float(string="Fuel Card", default_model="hr.contract")
    default_representation_fees = fields.Float(string="Representation Fees", default_model="hr.contract")
    default_internet = fields.Float(string="Internet", default_model="hr.contract")
    default_mobile = fields.Float(string="Mobile", default_model="hr.contract")
    default_meal_voucher_amount = fields.Float(string="Meal Vouchers", default_model="hr.contract")
    default_eco_checks = fields.Float(string="Eco Vouchers", default_model="hr.contract")
    onss_company_id = fields.Char(related='company_id.onss_company_id', readonly=False)
    onss_registration_number = fields.Char(related='company_id.onss_registration_number', readonly=False)
    dmfa_employer_class = fields.Char(related='company_id.dmfa_employer_class', readonly=False)
