import numpy
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

def boxblur(img):
    Is = Image.open(img)
    I = Is.convert('L')
    I = numpy.asarray(I)
    I = I / 255.0

    k_sharen = numpy.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
    '''
    0  -1  0
    -1  5 -1
    0  -1  0
    '''

    J = ndimage.convolve(I, k_sharen, mode='constant', cval=0.0)

    plt.figure(figsize = (15,15))

    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    plt.subplot(2,2,2)
    plt.imshow(J)
    plt.xlabel('Box Blur')

    plt.grid(False)
    plt.show()

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value

def padding_boxblur(img):
    Is = Image.open(img); # imagen del sudo
    I = Is.convert('L'); # se convierte a escala de grises
    I = numpy.asarray(I); # conversion numerica para poder operar de 0-1
    I = I / 255.0; # normalizacion 0 - 1

    I = numpy.pad(I, 10, pad_with, padder=0)

    k_sharen = numpy.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
    '''
    0  -1  0
    -1  5 -1
    0  -1  0
    '''
    
    J = ndimage.convolve(I, k_sharen, mode='constant', cval=0.0)

    plt.figure(figsize = (20,20))

    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    plt.subplot(2,2,2)
    plt.imshow(J)
    plt.xlabel('Padding Sharen')

    plt.grid(False)
    plt.show()

