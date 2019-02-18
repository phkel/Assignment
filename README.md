# First.py

## The main idea is based on this thread https://stackoverflow.com/questions/3407942/rgb-values-of-visible-spectrum. 

I imported the multispectral images using os and skimage.io libraries. Then converted the visible wavelengths to RGB values and added intensity correction. I didn't multiply the values with 255 because the original images are 16bit. Later on I found the new pixel values with RGB color components. Numpy library was used for creating arrays and PIL for saving the images. To see all the images with different wavelengths in RGB uncomment lines 74-76. Otherwise you will see the last image with wavelength 700 in RGB. 

# Second.py 

## The idea behind this calculations is to find the reflectance data from image -> XYZ -> RGB (https://medium.com/hipster-color-science/color-reproductions-of-hyperspectral-images-ad6210bbcd1d)

At first I did the same thing, imported the images with os and skimage.io libraries. Then made three different arrays – for color matching functions, illuminant D65 spectral power and XYZ to RGB transformation matrix. For every pixel in the image I found the XYZ coordinates and then used the XYZ to RGB matrix for calculating the data to RGB and saved it to new image. 

The example screenshot.png was my best shot for transforming but unfortunately I lost the code and I didn't git ☹️
