#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
from sys import argv

script, copy_from_path, copy_to_path = argv

sourcefile = open(copy_from_path)
pasted_content = sourcefile.read()
sourcefile.close()

destinationfile = open(copy_to_path,'r+')
destinationfile.write("\n"+pasted_content)
destinationfile.close()

print ("Copied the contents of %s into %s!" % (copy_from_path, copy_to_path))
