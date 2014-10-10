#coding=utf-8

class CustomerInfo:
	def __init__(self, args):
		self._name = str(args['name'])
		self._ref = str(args['ref'])

		self._street = str(args['address']['street'])
		self._postal = str(args['address']['postal'])
		self._city = str(args['address']['city'])

	def name(self):
		return self._name

	def ref(self):
		return self._ref

	def street(self):
		return self._street

	def postal(self):
		return self._postal

	def city(self):
		return self._city

if __name__ == "__main__":
	config = {
		"name":"Customer company name",
		"ref":"Customer reference",
		"address":{
			"street":"Customer street",
			"postal":"54321",
			"city":"Customer city"
		}
	}

	customerInfo = CustomerInfo(config)
	assert(customerInfo.name() == config['name'])
	assert(customerInfo.ref() == config['ref'])
	assert(customerInfo.street() == config['address']['street'])
	assert(customerInfo.postal() == config['address']['postal'])
	assert(customerInfo.city() == config['address']['city'])
