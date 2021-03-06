#coding=utf-8
import datetime

from product import *
from customer_info import *
from company_info import *
from general_spec import *
from invoice_spec import *

class Invoice(object):
	def __init__(self, content):
		self._json = content

		self._generalSpec = GeneralSpec(content['general_spec'])
		self._invoiceSpec = InvoiceSpec(content['invoice_spec'])
		self._companyInfo = CompanyInfo(content['company_info'])
		self._customerInfo = CustomerInfo(content['customer_info'])
		self._products = []
		for productArgs in content['products']:
			self._products.append(Product(productArgs))

		self.sumProducts()

	def generalSpec(self):
		return self._generalSpec

	def invoiceSpec(self):
		return self._invoiceSpec

	def companyInfo(self):
		return self._companyInfo

	def customerInfo(self):
		return self._customerInfo

	def products(self):
		return self._products

	# General Specifications
	def paymentTerms(self):
		return self.generalSpec().paymentTerms()

	# Invoice Specifications
	def companyRef(self):
		return self.invoiceSpec().ref()

	def invoiceDate(self):
		return self.invoiceSpec().invoiceDate()

	def invoiceId(self):
		return self.invoiceSpec().invoiceId()

	# Company information
	def companyName(self):
		return self.companyInfo().name()

	# Company Address
	def companyStreet(self):
		return self.companyInfo().street()

	def companyPostal(self):
		return self.companyInfo().postal()

	def companyCity(self):
		return self.companyInfo().city()

	# Company contact
	def companyPhone(self):
		return self.companyInfo().phone()

	def companyMobile(self):
		return self.companyInfo().mobile()

	def companyEmail(self):
		return self.companyInfo().email()

	def companyWeb(self):
		return self.companyInfo().web()

	# Company identification
	def companyOrgId(self):
		return self.companyInfo().orgId()

	def companyVatId(self):
		return self.companyInfo().vatId()

	def companyBankId(self):
		return self.companyInfo().bankId()

	# Customer information
	def customerName(self):
		return self.customerInfo().name()

	def customerRef(self):
		return self.customerInfo().ref()

	# Customer Address
	def customerStreet(self):
		return self.customerInfo().street()

	def customerPostal(self):
		return self.customerInfo().postal()

	def customerCity(self):
		return self.customerInfo().city()

	# Products
	def aggrProducts(self):
		resList = []
		for product in self.products():
			resDir = {}

			resDir['description'] = product.description()

			# Calculate sum
			sumExVat = product.priceNoVat() * product.quantity()
			resDir['sumExVat'] = str(product.priceNoVat() * product.quantity()).replace(".",",")

			# Calculate sum of vat
			sumVat = sumExVat * product.vat()
			resDir['sumVat'] = str(sumExVat * product.vat()).replace(".",",")

			# Calculate total sum including vat
			sumInclVat = sumExVat + sumVat
			resDir['sumInclVat'] = str(sumExVat + sumVat).replace(".",",")

			# Pretty Vat percentage
			prettyVat = "%d %%"%(product.vat()*100)
			resDir['prettyVat'] = str("%d %%"%(product.vat()*100)).replace(".",",")

			resDir['price_no_vat'] = str(product.priceNoVat()).replace(".", ",")

			resDir['quantity'] = str(product.quantity()).replace(".",",")

			resList.append(resDir)

		return resList

	def currency(self):
		return self.generalSpec().currency()

	def expirationDate(self):
		# invoice date + payment terms
		dt = datetime.timedelta(days=int(self.paymentTerms()))
		return self.invoiceSpec().invoiceDate() + dt

	def totalSum(self):
		return self._totalSum

	def totalVat(self):
		return self._totalVat

	def productSum(self):
		productSum = {}
		productSum['totalSum'] = str(self.totalSum()).replace(".",",")
		productSum['totalVat'] = str(self.totalVat()).replace(".",",")
		productSum['totalExclVat'] = str(self.totalSum() - self.totalVat()).replace(".",",")
		return productSum

	def sumProducts(self):
		self._totalSum = 0
		self._totalVat = 0
		for product in self.products():
			productSum = product.priceNoVat() * product.quantity()
			productVat = productSum * product.vat()
			productTotal = productSum + productVat
			self._totalSum += productTotal
			self._totalVat += productVat
