#coding=utf-8

from os import path
import os
import shutil

def createDir(directory):
	if path.exists(directory):
		if path.isdir(directory):
			print "Directory does already exists, nothing to do"
		else:
			print "A non directory with filename %s does already exists, please rename and try again"%(path.relpath(directory))
	else:
		os.makedirs(directory)

def copyFile(srcDir, dstDir, filename):
	# Copy CSS file to invoices directory
	src = path.join(srcDir, filename)
	dst = path.join(dstDir, filename)

	if not path.exists(src):
		print "Source file %s does not exist"%(src)
		return

	if path.exists(dst):
		print "Destination file %s does already exist"%(dst)

	shutil.copyfile(src, dst)

if __name__ == "__main__":
	# Create a dir invoice if not exists
	root = path.abspath("./")
	dstDirName = "invoices"
	dstDir = path.join(root, dstDirName)
	createDir(dstDir)

	srcDir = path.join(root, "swedish")
	cssfile = "invoice_style.css"
	logofile = "logo.png"
	copyFile(srcDir, dstDir, cssfile)
	copyFile(srcDir, dstDir, logofile)
	print "Installation complete"
