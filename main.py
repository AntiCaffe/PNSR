from PIL import Image
import numpy as np
import math
image1 = Image.open("C:\project\PNSR\Ysigon.jpg")
image2 = Image.open("C:\project\PNSR\cubic_Ysigon.jpg")
pix1 = np.array(image1, dtype=np.uint8)
pix2 = np.array(image2, dtype=np.uint8)
pix3 = (pix1-pix2)**2
R = 255.0
total = 0

print(total,pix3.sum())
MSE2 = np.mean((pix1-pix2)**2)
PSNR = 20*math.log10(R / math.sqrt(MSE2))
print("MANUAL_EXAMPLE_PSNR",PSNR)
################ MANUAL - EXAMPLE #######################
from skimage.metrics import peak_signal_noise_ratio
print("SK_PSNR")
print(peak_signal_noise_ratio(pix1,pix2))
import cv2
print("CV2_PSNR")
print(cv2.PSNR(pix1,pix2))