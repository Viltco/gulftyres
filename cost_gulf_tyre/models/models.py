# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GulfCostTyres(models.Model):
    _inherit = 'product.template'

    dot = fields.Integer(string="DOT")
    brand = fields.Char(string='Brand')
    wavrg = fields.Char(string='Wavrg')
    sale1 = fields.Char(string='Sale1', compute="compute_sale_walk_in")
    sale2 = fields.Char(string='Sale2', compute="compute_sale_credit")
    sale3 = fields.Char(string='Sale3', compute="compute_sale_cash")

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
    pur_dt=fields.Datetime(string="Pur-dt")

    # def compute_date_receipt(self):
    #     for i in self:
    #         date = self.env['stock.picking'].search([])
            # for j in date:
            #     for k in date.move_ids_without_package:
            #         if j.product_id.name == i.name:
            #             i.pur_dt = j.scheduled_date
            #             print('date', i.pur_dt)


    def compute_product_invoice_sale(self):
        for rec in self:
            total = 0
            qty = self.env['stock.picking'].search([])
            for i in qty:
                if i.state == 'assigned':
                    for j in i.move_line_ids_without_package:
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
            k.shj = 0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])
            for i in obj:

                if i.location_id.location_id.name == 'Shj' and i.product_id.id == k.id:
                    k.shj = i.quantity



    def compute_shjsm_location(self):
        for k in self:
            k.shjsm = 0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])

            for i in obj:
                print(i.product_id.name,i.quantity)
                if i.location_id.location_id.name == 'ShjSM' and i.product_id.id == k.id:
                    k.shjsm = i.quantity


    def compute_quz_location(self):
        for k in self:
            k.quz =0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])
            for i in obj:
                if i.location_id.location_id.name == 'Quz' and i.product_id.id == k.id:
                    k.quz = i.quantity



    def compute_ain_location(self):
        for k in self:
            k.ain = 0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])
            for i in obj:
                if i.location_id.location_id.name == 'Ain' and i.product_id.id == k.id:
                    k.ain = i.quantity



    def compute_ainw_location(self):
        for k in self:
            k.ainw = 0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])
            for i in obj:
                if i.location_id.location_id.name == 'AinW' and i.product_id.id == k.id:
                    k.ainw = i.quantity



    def compute_ajm_location(self):
        for k in self:
            k.ajm = 0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])
            for i in obj:
                if i.location_id.location_id.name == 'Ajm' and i.product_id.id == k.id:
                    k.ajm = i.quantity



    def compute_albr_location(self):
        for k in self:
            k.albr = 0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])
            for i in obj:
                if i.location_id.location_id.name == 'AlBr' and i.product_id.id == k.id:
                    k.albr = i.quantity



    def compute_ban_location(self):
        for k in self:
            k.ban = 0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])
            for i in obj:
                if i.location_id.location_id.name == 'BAN' and i.product_id.id == k.id:
                    print('hgf')
                    k.ban = i.quantity
                    print('pperftghj', i.quantity)



    def compute_abu_location(self):
        for k in self:
            k.abu = 0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])
            for i in obj:
                if i.location_id.location_id.name == 'ABU' and i.product_id.id == k.id:
                    k.abu = i.quantity



    def compute_abuold_location(self):
        for k in self:
            k.abuold = 0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])
            for i in obj:

                if i.location_id.location_id.name == 'ABUOL' and i.product_id.id == k.id:
                    k.abuold = i.quantity



    def compute_mzr_location(self):
        for k in self:
            k.mzr = 0
            obj = self.env['stock.quant'].search([('product_id', '=', k.id)])
            for i in obj:
                if i.location_id.location_id.name == 'MZR' and i.product_id.id == k.id:
                    k.mzr = i.quantity



    def compute_sale_walk_in(self):
        for i in self:
            total = 0
            obj = self.env['product.pricelist.item'].search([('name', '=', ''), ('pricelist_id.name', '=', 'Sale1')])
            for j in obj:
                total = j.fixed_price + total
            i.sale1 = total

    def compute_sale_credit(self):
        for i in self:
            total = 0
            obj = self.env['product.pricelist.item'].search([('name', '=', ''), ('pricelist_id.name', '=', 'Sale2')])
            for j in obj:
                total = j.fixed_price+total
            i.sale2 = total

    def compute_sale_cash(self):
        for i in self:
            total = 0
            obj = self.env['product.pricelist.item'].search([('name', '=', ''),('pricelist_id.name', '=', 'Sale3')])
            for j in obj:
                total = j.fixed_price + total
            i.sale3 = total


