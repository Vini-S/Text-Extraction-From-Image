
from PIL import Image

from pytesseract import image_to_string

image = Image.open("vinita.png")

text = image_to_string(image)

print(text)


