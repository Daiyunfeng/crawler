#!/usr/bin/python
# -*- coding: utf-8 -*-
from pytesseract import *
from PIL import Image
im = Image.open('test.png')
textcode = image_to_string(im,lang='chi_sim')
print(textcode)