import numpy as np
import pandas as pd
import os
import sys
import pyocr
import codecs
import pyocr.builders

from pathlib import Path
from PIL import Image

input_path = Path('input')

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit()
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
lang = langs[0]

builder = pyocr.builders.LineBoxBuilder()

def convert(pic):
    output_path = Path('output')
    k = pic.stem + '.html'
    output_file = output_path / k

    line_boxes = tool.image_to_string(
        Image.open(pic),
        lang = lang,
        builder = builder
    )

    with codecs.open(output_file, 'w', encoding='utf-8') as file_descriptor:
        builder.write_file(file_descriptor, line_boxes)

for x in input_path.iterdir():
    convert(x)

print('Conversion Done!')