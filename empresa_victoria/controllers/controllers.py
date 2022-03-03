# -*- coding: utf-8 -*-
# from odoo import http


# class EmpresaVictoria(http.Controller):
#     @http.route('/empresa_victoria/empresa_victoria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empresa_victoria/empresa_victoria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('empresa_victoria.listing', {
#             'root': '/empresa_victoria/empresa_victoria',
#             'objects': http.request.env['empresa_victoria.empresa_victoria'].search([]),
#         })

#     @http.route('/empresa_victoria/empresa_victoria/objects/<model("empresa_victoria.empresa_victoria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empresa_victoria.object', {
#             'object': obj
#         })
