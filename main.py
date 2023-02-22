# convert whole jpg folder to png
import sys
import os
from PIL import Image
import re

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(f'{image_folder}{output_folder}'):
    os.makedirs(f'{image_folder}{output_folder}')

for filename in os.listdir(image_folder):
    # print(filename)
    pattern = r'\.jpg$'
    # check if the file is jpg file
    if re.search(pattern, filename):
        img = Image.open(f'{image_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        # this will remove the .jpg from the end of the name
        img.save(f'{image_folder}{output_folder}{clean_name}.png', 'png')

print('All done')
print(f'Check this folder for output: {image_folder}{output_folder}')
