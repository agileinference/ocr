import numpy as np
import pandas as pd
from PIL import Image
import os
import pyocr
import codecs
import pyocr.builders

pic = 'C:/Users/jansc/Pictures/ocr_test.png'

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage

print(tools)
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))

txt = tool.image_to_string(
    Image.open(pic),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
builder = pyocr.builders.LineBoxBuilder()
line_boxes = tool.image_to_string(
    Image.open(pic),
    lang=lang,
    builder=builder
)

line_and_word_boxes = tool.image_to_string(
    Image.open(pic), lang="eng",
    builder=pyocr.builders.LineBoxBuilder()
)

digits = tool.image_to_string(
    Image.open(pic),
    lang=lang,
    builder=pyocr.tesseract.DigitBuilder()
)

with codecs.open("output.html", 'w', encoding='utf-8') as file_descriptor:
    builder.write_file(file_descriptor, line_boxes)
with codecs.open("output.html", 'r', encoding='utf-8') as file_descriptor:
    line_boxes = builder.read_file(file_descriptor)

