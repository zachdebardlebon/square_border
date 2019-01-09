import sys
from PIL import Image, ImageOps

filename = sys.argv[1]
border_size = int(sys.argv[2]) if len(sys.argv) > 2 else 100
border_color = int(sys.argv[3], 16) if len(sys.argv) > 3 else  0xFFFFFF

image = Image.open(filename)
border = ImageOps.expand(image, border_size, border_color)
border.save(filename.split('.')[0] + "_border.png")
