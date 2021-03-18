# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GulfCostTyres(models.Model):
    _inherit = 'product.template'


    # reserve_stock_count = fields.Float("Reserve Stock")

    dot = fields.Integer(string="DOT")
    brand = fields.Char(string='Brand')
    wavrg = fields.Char(string='Wavrg')
    sale1 = fields.Char(string='Sale 1 (Walk-in)', compute="compute_sale_walk_in")
    sale2 = fields.Char(string='Sale 2 (Credit)', compute="compute_sale_credit")
    sale3 = fields.Char(string='Sale 3 (Cash)', compute="compute_sale_cash")

    # locations

    shj = fields.Float(string='Shj', compute="compute_shj_location")
    shjsm = fields.Float(string='ShjSM', compute="compute_shjsm_location")
    quz = fields.Float(string='Quz', compute="compute_quz_location")
    ain = fields.Float(string='Ain', compute="compute_ain_location")
    ainw = fields.Float(string='AinW', compute="compute_ainw_location")
    ajm = fields.Float(string='Ajm', compute="compute_ajm_location")
    albr = fields.Float(string='AlBr', compute="compute_albr_location")
    ban = fields.Float(string='BAN', compute="compute_ban_location")
    abu = fields.Float(string='ABU', compute="compute_abu_location")
    abuold = fields.Float(string='ABUOLD', compute="compute_abuold_location")
    mzr = fields.Float(string='MZR', compute="compute_mzr_location")

    res_stk = fields.Float(string="Res-Stk")
    p_inv = fields.Float(string="P-Inv", compute="compute_product_invoice_sale")
    pur_qty = fields.Float(string="Pur-Qty", compute="compute_product_invoice_purchase")

    def compute_product_invoice_sale(self):
        for rec in self:
            total = 0
            qty = self.env['stock.picking'].search([])
            for i in qty:
                if i.state == 'assigned':
                    for j in i.move_line_ids_without_package:
                        print('erty', j.product_id.name)
                        if j.product_id.name == rec.name:
                            total = j.product_uom_qty + total
            rec.p_inv = total

    def compute_product_invoice_purchase(self):
        for rec in self:
            total = 0
            qty = self.env['stock.picking'].search([])
            for i in qty:
                if i.state == 'assigned':
                    for j in qty.move_ids_without_package:
                        if j.product_id.name == rec.name:
                            total = j.product_uom_qty + total
            rec.pur_qty = total


    def compute_shj_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Shj':
                    k.shj = i.available_quantity
                else:
                    k.shj

    def compute_shjsm_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Shjsm':
                    k.shjsm = i.available_quantity
                else:
                    k.shjsm

    def compute_quz_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Quz':
                    k.quz = i.available_quantity
                else:
                    k.quz

    def compute_ain_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Ain':
                    k.ain = i.available_quantity
                else:
                    k.ain

    def compute_ainw_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Ainw':
                    k.ainw = i.available_quantity
                else:
                    k.ainw

    def compute_ajm_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Ajm':
                    k.ajm = i.available_quantity
                else:
                    k.ajm

    def compute_albr_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Albr':
                    k.albr = i.available_quantity
                else:
                    k.albr

    def compute_ban_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Ban':
                    k.ban = i.available_quantity
                else:
                    k.ban

    def compute_abu_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Abu':
                    k.abu = i.available_quantity
                else:
                    k.abu

    def compute_abuold_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Abuold':
                    k.abuold = i.available_quantity
                else:
                    k.abuold

    def compute_mzr_location(self):
        for k in self:
            obj = self.env['stock.quant'].search([])
            for i in obj:
                if i.location_id.name == 'Mzr':
                    k.mzr = i.available_quantity
                else:
                    k.mzr

    def compute_sale_walk_in(self):
        for i in self:
            total = 0
            obj = self.env['product.pricelist.item'].search([('name', '=', ''),
                                                        ('pricelist_id.name', '=', 'walk-in')])
            for j in obj:
                total = j.fixed_price + total
            i.sale1 = total

    def compute_sale_credit(self):
        for i in self:
            total = 0
            obj = self.env['product.pricelist.item'].search([('name', '=', ''),
                                                             ('pricelist_id.name', '=', 'Credit')])

            for j in obj:
                total = j.fixed_price+total
            i.sale2 = total

    def compute_sale_cash(self):
        for i in self:
            total = 0
            obj = self.env['product.pricelist.item'].search([('name', '=', ''),
                                                             ('pricelist_id.name', '=', 'Cash')])

            for j in obj:
                total = j.fixed_price + total
            i.sale3 = total










