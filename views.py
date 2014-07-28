#coding=utf-8
class Invoice(object):
	def __init__(self, content):
		self._json = content
		self._json['product_aggr'] = {}
		self.sumProducts()
	
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

	def customerRef(self):
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
		totalSum = 0.0
		totalVat = 0.0

		for product in self._json['products']:
			# Calculate sum
			product['sumExVat'] = product['price_no_vat'] * product['quantity']

			# Calculate sum of vat
			product['sumVat'] = product['sumExVat'] * product['vat']

			# Calculate total sum including vat
			product['sumInclVat'] = product['sumExVat'] + product['sumVat']

			# Pretty Vat percentage
			product['prettyVat'] = "%d %%"%(product['vat']*100)

			#Overhead aggregation
			totalSum += product['sumExVat']
			totalVat += product['sumVat']

		return self._json['products']

	def currency(self):
		return self._json['general_spec']['currency']

	def product_aggr(self):
		self._json['product_aggr']['totalSum'] = self._totalSum
		self._json['product_aggr']['totalVat'] = self._totalVat
		return self._json['product_aggr']
	
	# Helper functions
	def dateToString(self, json):
		return "%d-%d-%d"%(json['year'], json['month'], json['day'])

	def sumProducts(self):
		self._totalSum = 0
		self._totalVat = 0
		for product in self._json['products']:
			self._totalSum += product['price_no_vat'] * product['quantity']
			self._totalVat += self._totalSum * product['vat']
