#coding=utf-8

from os import path
import os

if __name__ == "__main__":
	# Create a dir invoice if not exists
	root = path.abspath("./")
	directory = path.join(root, "invoices")
	if path.exists(directory):
		if path.isdir(directory):
			print "Directory does already exists, nothing to do"
		else:
			print "A non directory with filename %s does already exists, please rename and try again"%(path.relpath(directory))
	else:
		os.makedirs(directory)
		print "Installation complete"
