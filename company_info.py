#coding=utf-8

class CompanyInfo:
	def __init__(self, args):
		self._name = str(args['name'])

		self._street = str(args['address']['street'])
		self._postal = str(args['address']['postal'])
		self._city = str(args['address']['city'])

		self._phone = str(args['contact']['phone'])
		self._mobile = str(args['contact']['mobile'])
		self._email = str(args['contact']['email'])
		self._web = str(args['contact']['web'])

		self._orgId = str(args['id']['org_id'])
		self._vatId = str(args['id']['vat_id'])
		self._bankId = str(args['id']['bank_id'])

	def name(self):
		return self._name

	def street(self):
		return self._street

	def postal(self):
		return self._postal

	def city(self):
		return self._city

	def phone(self):
		return self._phone

	def mobile(self):
		return self._mobile

	def email(self):
		return self._email

	def web(self):
		return self._web

	def orgId(self):
		return self._orgId

	def vatId(self):
		return self._vatId

	def bankId(self):
		return self._bankId

if __name__ == "__main__":
	config = {
		"name":"My company",
		"address":{
			"street":"Company street",
			"postal":"12345",
			"city":"Company city"
		},

		"contact":{
			"phone":"08-123 45 67",
			"mobile":"070-123 45 67",
			"email":"info@company.com",
			"web":"company.com"
		},

		"id":{
			"org_id":"123456-789",
			"vat_id":"SE12345678901",
			"bank_id":"1234-5678"
		}
	}

	companyInfo = CompanyInfo(config)
	assert(companyInfo.name() == config['name'])

	assert(companyInfo.street() == config['address']['street'])
	assert(companyInfo.postal() == config['address']['postal'])
	assert(companyInfo.city() == config['address']['city'])

	assert(companyInfo.phone() == config['contact']['phone'])
	assert(companyInfo.mobile() == config['contact']['mobile'])
	assert(companyInfo.email() == config['contact']['email'])
	assert(companyInfo.web() == config['contact']['web'])

	assert(companyInfo.orgId() == config['id']['org_id'])
	assert(companyInfo.vatId() == config['id']['vat_id'])
	assert(companyInfo.bankId() == config['id']['bank_id'])
