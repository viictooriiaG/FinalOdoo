# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class empresa_victoria(models.Model):
#     _name = 'empresa_victoria.empresa_victoria'
#     _description = 'empresa_victoria.empresa_victoria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date 

class empresa(models.Model):
	_name = 'empresa_victoria.empresa'
	_description = 'model empresa'

	name = fields.Char('NIF',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	telefono = fields.Char(string='Teléfono',required=True)

class trabajador(models.Model):
	_name = 'empresa_victoria.trabajador'
	_description = 'model trabajador'
	fecha_nacimiento = fields.Date(string='Fecha de nacimiento',required=True)
	fecha_nacimiento = fields.Date(string='Fecha de nacimiento',required=True)
	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	telefono = fields.Char(string='Teléfono',required=True)
	annos = fields.Integer("Años", compute="_get_annos")

class materiales(models.Model):
	_name = 'empresa_victoria.materiales'
	_description = 'model materiales'

	name = fields.Char('ID_producto',required=True)
	producto = fields.Char(string='Producto',required=True)
	descripcion = fields.Char(string='Descripcion',required=True)
	cantidadv = fields.Integer(string='cantidadv',required=True)
	preciov = fields.Integer(string='preciov',required=True)
	totalv = fields.Integer("Total_Venta", compute="_get_totalv")
	materiales_fabricante_ids=fields.One2many('empresa_victoria.fabricantes','fabricantes_materiales_id', string='material')



class fabricantes(models.Model):
	_name = 'empresa_victoria.fabricantes'
	_description = 'model fabricantes'

	name = fields.Char('ID_fabricante',required=True)
	producto = fields.Char(string='Producto',required=True)
	descripcion = fields.Char(string='Descripcion',required=True)
	cantidadc = fields.Integer(string='cantidadc',required=True)
	precioc = fields.Integer(string='precioc',required=True)
	totalc = fields.Integer("Total_Costo", compute="_get_totalc")
	fabricantes_materiales_id=fields.Many2one('empresa_victoria.materiales',string='fabricante')


	@api.depends('fecha_nacimiento')
	def _get_annos(self):
		for pers in self:
			hoy=date.today()
			pers.annos = relativedelta(hoy, pers.fecha_nacimiento).years

	@api.depends('preciov')
	def _get_totalv(self):
		for mat in self:
			mat.totalv =  mat.preciov * mat.cantidadv

	@api.depends('precioc')
	def _get_totalc(self):
		for fab in self:
			fab.totalc =  fab.precioc * fab.cantidadc