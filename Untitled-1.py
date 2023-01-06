from PIL import Image
import numpy as np
image1 = Image.open("Ysigon.jpg")
image2 = Image.open("cubic_Ysigon.jpg")
pix1 = np.array(image1, dtype=np.uint8)
pix2 = np.array(image2, dtype=np.uint8)
print(pix1.size,pix2.size)