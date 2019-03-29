#!/usr/bin/python3
from PIL import Image
import sys

name = sys.argv[1]

names = ['drawable-hdpi-icon.png', 'drawable-mdpi-icon.png', 'drawable-ldpi-icon.png', 'drawable-xxhdpi-icon.png', 'drawable-xhdpi-icon.png', 'drawable-xxxhdpi-icon.png']
sizes = [72, 48, 36, 144, 96, 192]

for i in range(len(names)):
	img = Image.open(name)
	img.thumbnail((sizes[i], sizes[i]))
	img.save(names[i])


#by koza-azaza
