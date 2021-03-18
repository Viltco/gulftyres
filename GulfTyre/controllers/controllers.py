# -*- coding: utf-8 -*-
# from odoo import http


# class Gulfcosttyres(http.Controller):
#     @http.route('/gulfcosttyres/gulfcosttyres/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gulfcosttyres/gulfcosttyres/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gulfcosttyres.listing', {
#             'root': '/gulfcosttyres/gulfcosttyres',
#             'objects': http.request.env['gulfcosttyres.gulfcosttyres'].search([]),
#         })

#     @http.route('/gulfcosttyres/gulfcosttyres/objects/<model("gulfcosttyres.gulfcosttyres"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gulfcosttyres.object', {
#             'object': obj
#         })
