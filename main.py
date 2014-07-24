#coding=utf-8

#imports
import pystache as ps
import json
from views import Invoice

def main():
	# Load JSON config
	# Create Invoice with JSON dictionary
	f = open("invoice.json", "r")
	file_content = f.read()
	content = json.loads(file_content)
	invoice = Invoice(content)
	renderer = ps.Renderer(file_encoding="utf-8", string_encoding="utf-8")
	html = renderer.render(invoice)
	fout = open("invoice.html", "w")
	fout.write(html.encode("UTF-8"))

if __name__ == "__main__":
	main()
