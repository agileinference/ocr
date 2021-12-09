import sys
import pyocr
import codecs
import pyocr.builders

from pathlib import Path
from PIL import Image

input_path = Path('input')

#check if OCR tools exists
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit()
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
lang = langs[0]

builder = pyocr.builders.LineBoxBuilder()

#main conversion function
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

n=0
i=0

#count number of items in input directory
for files in input_path.iterdir():
    n=n+1
    
if n>0:
    for x in input_path.iterdir():
        convert(x)
        i = i+1
        print('Converting',x.stem, '(',i, 'out of',n,')')
    print('Conversion Done!')
else:
    print('Inout directory is empty.')