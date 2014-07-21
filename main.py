#coding:utf-8

#imports
import pystache as ps
import json
from views import Invoice

def main():
	# Load JSON config
	# Create Invoice with JSON dictionary
	f = open("invoice.json", "r")
	file_content = f.read()
	print file_content
	content = json.loads(file_content)
	print content
	invoice = Invoice(content)
	renderer = ps.Renderer()
	print renderer.render(invoice)

if __name__ == "__main__":
	main()
