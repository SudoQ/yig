#coding=utf-8

import datetime

class InvoiceSpec:
	def __init__(self, args):
		self._ref = str(args['ref'])
		self._invoiceId = str(args['invoice_id'])

		year = int(args['invoice_date']['year'])
		month = int(args['invoice_date']['month'])
		day = int(args['invoice_date']['day'])

		self._invoiceDate = datetime.date(year, month, day)

	def ref(self):
		return self._ref

	def invoiceId(self):
		return self._invoiceId

	def invoiceDate(self):
		return self._invoiceDate

if __name__ == "__main__":
	config = {
		"ref":"Company reference",
		"invoice_date":{
			"year": 2014,
			"month": 7,
			"day": 21
		},
		"invoice_id":"14072101"
	}

	invoiceSpec = InvoiceSpec(config)
	assert(invoiceSpec.ref() == config['ref'])
	assert(invoiceSpec.invoiceDate() == datetime.date(2014, 7, 21))
	assert(invoiceSpec.invoiceId() == config['invoice_id'])
