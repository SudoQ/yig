#coding=utf-8

#imports
import pystache as ps
import sys
import json
from views import Invoice

def main():
	configFile = "invoice.json"
	htmlFile = "invoice.html"
	if len(sys.argv) == 2 :
		configFile = sys.argv[1]
		htmlFile = configFile[:-4] + "html"

	f = open(configFile, "r")
	file_content = f.read()
	content = json.loads(file_content)
	invoice = Invoice(content)
	renderer = ps.Renderer(file_encoding="utf-8", string_encoding="utf-8")
	html = renderer.render(invoice)
	fout = open(htmlFile, "w")
	fout.write(html.encode("UTF-8"))

if __name__ == "__main__":
	main()
