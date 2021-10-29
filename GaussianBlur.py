import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

def gaussianBlur(imagename):
    Is = Image.open(imagename)
    I = Is.convert('L')
    I = numpy.asarray(I)
    I = I / 255.0

    k0 = numpy.array([[1,2,1],[2,4,2],[1,2,1]])
    k0 = k0 * (1/16)

    J0 = ndimage.convolve(I, k0, mode='constant', cval=0.0)

    plt.figure(figsize = (15,15))

    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    plt.subplot(2,2,2)
    plt.imshow(J0)
    plt.xlabel('Gaussian Blur 3x3')


    plt.grid(False)
    plt.show()

def boxBlur(imagename):
    Is = Image.open(imagename)
    I = Is.convert('L')
    I = numpy.asarray(I)
    I = I / 255.0

    k0 = numpy.array([[1,1,1],[1,1,1],[1,1,1]])
    k0 = k0 * (1/9)

    J0 = ndimage.convolve(I, k0, mode='constant', cval=0.0)

    plt.figure(figsize = (15,15))

    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    plt.subplot(2,2,2)
    plt.imshow(J0)
    plt.xlabel('Box Blur')


    plt.grid(False)
    plt.show()

def edgeDetection2(imagename):
    Is = Image.open(imagename)
    I = Is.convert('L')
    I = numpy.asarray(I)
    I = I / 255.0

    k0 = numpy.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

    J0 = ndimage.convolve(I, k0, mode='constant', cval=0.0)

    plt.figure(figsize = (15,15))

    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    plt.subplot(2,2,2)
    plt.imshow(J0)
    plt.xlabel('Edge Detection 2')


    plt.grid(False)
    plt.show()
    
gaussianBlur('batita.png')
boxBlur('batita.png')
edgeDetection2('batita.png')