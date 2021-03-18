# -*- coding: utf-8 -*-
# from odoo import http


# class Gulftyrescost(http.Controller):
#     @http.route('/gulftyrescost/gulftyrescost/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gulftyrescost/gulftyrescost/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gulftyrescost.listing', {
#             'root': '/gulftyrescost/gulftyrescost',
#             'objects': http.request.env['gulftyrescost.gulftyrescost'].search([]),
#         })

#     @http.route('/gulftyrescost/gulftyrescost/objects/<model("gulftyrescost.gulftyrescost"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gulftyrescost.object', {
#             'object': obj
#         })
