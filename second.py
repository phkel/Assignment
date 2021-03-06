import os
import imageio
import skimage.io as ski
import numpy as np
from PIL import Image

path = "multispectral_images/"
dirs = os.listdir(path)
im = ski.imread_collection('multispectral_images/*.png')

# CIE 1931 XYZ color space color matching functions
xyz = np.array([[0.014310, 0.00096, 0.067850],
[0.043510, 0.001210, 0.207400],
[0.134380, 0.004000, 0.645600],
[0.283900, 0.011600, 1.385600],
[0.348280, 0.023000, 1.747060],
[0.336200, 0.038000, 1.772110],
[0.290800, 0.060000, 1.669200],
[0.195360, 0.090980, 1.287640],
[0.095640, 0.139020, 0.812950],
[0.032010, 0.208020, 0.465180],
[0.004900, 0.323000, 0.272000],
[0.009300, 0.503000, 0.158200],
[0.063270, 0.710000, 0.078250],
[0.165500, 0.862000, 0.042160],
[0.290400, 0.954000, 0.020300],
[0.433450, 0.994950, 0.008750],
[0.594500, 0.995000, 0.003900],
[0.762100, 0.952000, 0.002100],
[0.916300, 0.870000, 0.001650],
[1.026300, 0.757000, 0.001100],
[1.062200, 0.631000, 0.000800],
[1.002600, 0.503000, 0.000340],
[0.854450, 0.381000, 0.000190],
[0.642400, 0.265000, 0.000050],
[0.447900, 0.175000, 0.000020],
[0.283500, 0.107000, 0.000000],
[0.164900, 0.061000, 0.000000],
[0.087400, 0.032000, 0.000000],
[0.046770, 0.017000, 0.000000],
[0.022700, 0.008210, 0.000000],
[0.011359, 0.004102, 0.000000]])

# Relative spectral power distribution of CIE standard illuminant D65 
D65 = [
  82.7549, 91.486, 93.4318, 86.6823, 104.865, 117.008,
  117.812, 114.861, 115.923, 108.811, 109.354, 107.802, 
  104.79, 107.689, 104.405, 104.046, 100, 96.3342, 
  95.788, 88.6856, 90.0062, 89.5991, 87.6987, 83.2886, 
  83.6992, 80.0268, 80.2146, 82.2778, 78.2842, 69.7213,
  71.6091]

# CIE XYZ to RGB transformation matrix 
to = np.array([[ 2.3706743, -0.9000405, -0.4706338], 
  [-0.5138850,  1.4253036,  0.0885814], 
  [0.0052982, -0.0146949,  1.0093968]])

# Image shape
width, height = im[0].shape

# Bands array
band = [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500,
510, 520, 530, 540, 550, 560, 570, 580, 590, 600,
610, 620, 630, 640, 650, 660, 670, 680, 690, 700]
bands = len(band) - 1

# Create new numpy array image 
image = np.zeros([512, 512, 3], dtype=np.uint8)

# Calculate the XYZ at first and then corresponding RGB values
for b in range(bands): 
  for w in range(width):
    for h in range(height):
      # Find CIE XYZ coordinates 
      X = xyz[b][0] * im[b][w,h] * D65[b] / 255
      Y = xyz[b][1] * im[b][w,h] * D65[b] / 255
      Z = xyz[b][2] * im[b][w,h] * D65[b] / 255
      # print('imageess', X, Y, Z)
      R = ((to[0][0] * X) + (to[0][1] * Y) + (to[0][2] * Z))
      G = ((to[1][0] * X) + (to[1][1] * Y) + (to[1][2] * Z))
      B = ((to[2][0] * X) + (to[2][1] * Y) + (to[2][2] * Z))
      #print('imageess', R, G, B)
      if R < 0:
        R = 0
      elif R > 255:
        R = 255 

      if G < 0:
        G =  abs(G)
      elif G > 255:
        G = 255 

      if B < 0:
        B = 0
      elif B > 255:
        B = 255 
      image[w,h] = (int(R), int(G), int(B))

# Save the last image 
img = Image.fromarray(image, 'RGB')
img.save('second.png')
img.show()

print('image', image.shape)

