import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

def gaussianBlur(imagename):
    Is = Image.open(imagename)
    I = Is.convert('L')
    I = numpy.asarray(I)
    I = I / 255.0

    def pad_with(vector, pad_width, iaxis, kwargs):
        pad_value = kwargs.get('padder', 10)
        vector[:pad_width[0]] = pad_value
        vector[-pad_width[1]:] = pad_value

    I = numpy.pad(I, 10, pad_with, padder=0)

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
    
