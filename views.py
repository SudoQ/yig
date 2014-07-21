class Invoice(object):
	def __init__(self, content):
		self._buyer = content['customer_info']['name']
		self._seller = content['company_info']['name']

	def buyer(self):
		return self._buyer

	def seller(self):
		return self._seller
