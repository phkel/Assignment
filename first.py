import os
import skimage.io as ski
import numpy as np
from PIL import Image

path = "multispectral_images/"
dirs = os.listdir(path)
im = ski.imread_collection('multispectral_images/*.png')
width, height = im[0].shape

band = [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700]
bands = len(band) - 1

# Code for RGB components for Visible Wavelengths: http://www.physics.sfasu.edu/astro/color/spectra.html 
for b in range(bands): 
  w = band[b]
  if w >= 380 and w < 440:
    R = -(w - 440) / (440 - 350)
    G = 0.0
    B = 1.0
  elif w >= 440 and w < 490:
    R = 0.0
    G = (w - 440) / (490 - 440)
    B = 1.0
  elif w >= 490 and w < 510:
    R = 0.0
    G = 1.0
    B = -(w - 510) / (510. - 490)
  elif w >= 510 and w < 580:
    R = (w - 510) / (580. - 510)
    G = 1.0
    B = 0.0
  elif w >= 580 and w < 645:
    R = 1.0
    G = -(w - 645) / (645. - 580)
    B = 0.0
  elif w >= 645 and w <= 780:
    R = 1.0
    G = 0.0
    B = 0.0
  else:
    R = 0.0
    G = 0.0
    B = 0.0

  # Intensity correction
  if w > 700:
    SSS = 0.3 + 0.7 * (780 - w) / (780 - 700)
  elif w < 420:
    SSS = 0.3 + 0.7 * (w - 380) / (420 - 380)
  else:
    SSS = 1

  R = R * SSS
  G = G * SSS
  B = B * SSS
  
  # Create new numpy array image 
  pixels = np.zeros([512, 512, 3], dtype=np.uint8)

  for w in range(width):
    for h in range(height):
      pixel = im[b][w,h]

      # Change gray values to RGB 
      red =   pixel * R
      green = pixel * G
      blue =  pixel * B
      pixels[w,h] = (int(red), int(green), int(blue))

  # All the images with different wavelengths in RGB
  # img = Image.fromarray(pixels, 'RGB')
  # img.save('my.png')
  # img.show()

img = Image.fromarray(pixels, 'RGB')
img.save('first.png')
img.show()

print('The image shown is the last one with wavelength 700 in RGB and its shape is:', pixels.shape, 'and type:', pixels.dtype)