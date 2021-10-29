import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

def pad_with(vector, pad_width, iaxis, kwargs):
        pad_value = kwargs.get('padder', 10)
        vector[:pad_width[0]] = pad_value
        vector[-pad_width[1]:] = pad_value

def edgeDet1(img):
    #Se inicializa la imagen
    Is = Image.open(img)
    I = Is.convert('L')
    I = numpy.asarray(I)
    I = I / 255.0

    I = numpy.pad(I, 30, pad_with, padder=1)

    #kernel Edge Detection version 1
    k = numpy.array([[1, 0, -1], [0, 0, 0], [-1, 0, 1]])

    #Convolucion
    J = ndimage.convolve(I, k, mode='constant', cval=0.0)

    #Plot
    plt.figure(figsize = (15,15))

    #Inserta la imagen original
    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Imagen original')
    
    #Inserta imagen convolucionada
    plt.subplot(2,2,2)
    plt.imshow(J)
    plt.xlabel('Edge Detection 1')

    #Imprime las imagenes
    plt.grid(False)
    plt.show()

