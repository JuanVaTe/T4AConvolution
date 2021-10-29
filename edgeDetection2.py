import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

def edgeDetection2(imagename):
    Is = Image.open(imagename)
    I = Is.convert('L')
    I = numpy.asarray(I)
    I = I / 255.0

    def pad_with(vector, pad_width, iaxis, kwargs):
        pad_value = kwargs.get('padder', 10)
        vector[:pad_width[0]] = pad_value
        vector[-pad_width[1]:] = pad_value

    I = numpy.pad(I, 10, pad_with, padder=0)

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
