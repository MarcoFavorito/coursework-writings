
import os
from PIL import Image

for p in os.listdir("."):
    if p[-4:]!=".png":
        continue
    img = Image.open(p)
    w, h = img.size
    img.crop((24,24,308,230)).save(p)