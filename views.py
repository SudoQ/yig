#coding=utf-8
class Invoice(object):
	def __init__(self, content):
		self._json = content
	
	# General Specifications
	def paymentTerms(self):
		return self._json['general_spec']['payment_terms']
	
	# Invoice Specifications
	def companyRef(self):
		return self._json['invoice_spec']['ref']

	def invoiceDate(self):
		return self.dateToString(self._json['invoice_spec']['invoice_date'])

	def invoiceId(self):
		return self._json['invoice_spec']['invoice_id']

	# Company information	
	def companyName(self):
		return self._json['company_info']['name']
	
	# Company Address
	def companyStreet(self):
		return self._json['company_info']['address']['street']

	def companyPostal(self):
		return self._json['company_info']['address']['postal']

	def companyCity(self):
		return self._json['company_info']['address']['city']

	# Company contact
	def companyPhone(self):
		return self._json['company_info']['contact']['phone']

	def companyMobile(self):
		return self._json['company_info']['contact']['mobile']

	def companyEmail(self):
		return self._json['company_info']['contact']['email']

	def companyWeb(self):
		return self._json['company_info']['contact']['web']

	# Company identification
	def companyOrgId(self):
		return self._json['company_info']['id']['org_id']

	def companyVatId(self):
		return self._json['company_info']['id']['vat_id']

	def companyBankId(self):
		return self._json['company_info']['id']['bank_id']

	# Customer information	
	def customerName(self):
		return self._json['customer_info']['name']

	def customRef(self):
		return self._json['customer_info']['ref']

	# Customer Address
	def customerStreet(self):
		return self._json['customer_info']['address']['street']

	def customerPostal(self):
		return self._json['customer_info']['address']['postal']

	def customerCity(self):
		return self._json['customer_info']['address']['city']

	# Products

	def products(self):
		return self._json['products']

	# Helper functions
	def dateToString(self, json):
		return "%d-%d-%d"%(json['year'], json['month'], json['day'])
