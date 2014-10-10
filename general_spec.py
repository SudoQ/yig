#coding=utf-8

class GeneralSpec:
	def __init__(self, args):
		self._paymentTerms = int(args['payment_terms'])
		self._currency = str(args['currency'])
		self._vat = float(args['vat'])

	def paymentTerms(self):
		return self._paymentTerms

	def currency(self):
		return self._currency

	def vat(self):
		return self._vat

	def prettyVat(self):
		vat = self.vat() * 100
		if int(vat) == float(vat) :
			vat = int(vat)

		return str(vat) + " %"

if __name__ == "__main__":
	config = {
		"payment_terms":30,
		"currency":"SEK",
		"vat":0.25
	}

	genSpec = GeneralSpec(config)
	assert(genSpec.paymentTerms() == config['payment_terms'])
	assert(genSpec.currency() == config['currency'])
	assert(genSpec.vat() == config['vat'])
	assert(genSpec.prettyVat() == "25 %")

	config['vat'] = 0.125
	genSpec = GeneralSpec(config)
	assert(genSpec.prettyVat() == "12.5 %")
