#coding=utf-8

class Product:
	def __init__(self, args):
		self._description = str(args['description'])
		self._priceNoVat = float(args['price_no_vat'])
		self._quantity = float(args['quantity'])
		self._vat = float(args['vat'])

	def description(self):
		return self._description

	def priceNoVat(self):
		return self._priceNoVat

	def quantity(self):
		return self._quantity

	def vat(self):
		return self._vat

	def priceWithVat(self):
		return self.priceNoVat() * (1.0 + self.vat())

if __name__ == "__main__":
	config = {
		"description": "A nice product",
		"price_no_vat": 100.0,
		"quantity": 2,
		"vat": 0.25
	}
	prod = Product(config)
	assert(prod.description() == config['description'])
	assert(prod.priceNoVat() == config['price_no_vat'])
	assert(prod.quantity() == config['quantity'])
	assert(prod.vat() == config['vat'])
	assert(prod.priceWithVat() == 125.0)

