#!/usr/bin/env python
# -*-coding:utf-8 -*-
import os, sys

if len(sys.argv) < 3:
    print("usage: "+sys.argv[0]+" <labels_folder> <images_folder>")
    sys.exit()


lable_path = sys.argv[1]
image_path = sys.argv[2]
image_filelist = os.listdir(image_path)
lable_filelist = os.listdir(lable_path)

try:

	count=0

	print(image_filelist)

	for file in image_filelist:
		print(file)
	for file in image_filelist:
		
		number=str(count).zfill(4)
		filename=os.path.splitext(file)[0]
		filetype=os.path.splitext(file)[1]

		old_imagefile = os.path.join(image_path, file)
		new_imagefile=os.path.join(image_path, number+filetype)
		os.rename(old_imagefile,new_imagefile)
		
		old_txtfile = os.path.join(lable_path, filename + ".txt")
		new_txtfile = os.path.join(lable_path, number+".txt")
		os.rename(old_txtfile,new_txtfile)
	  

		count+=1
except:
        s = sys.exc_info()
        print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))



