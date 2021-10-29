#Librerías
import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

#Crear padding en la imágen
def pad_with(vector, pad_width, iaxis, kwargs):

    pad_value = kwargs.get('padder', 10)

    vector[:pad_width[0]] = pad_value

    vector[-pad_width[1]:] = pad_value

def sharpen(img):

    #Inicializar imagen
    Is = Image.open(img)

    I = Is.convert('L')

    I = numpy.asarray(I)

    I = I / 255.0

    I = numpy.pad(I, 30, pad_with, padder=1)

    #Kernel Sharpen
    k = numpy.array([[0,-1,0],[-1,5,1],[0,-1,0]])

    #Convolución
    J = ndimage.convolve(I, k, mode='constant', cval=0.0)

    #Gráfica
    plt.figure(figsize = (15,15))

    #Imagen original
    plt.subplot(2,2,1)

    plt.imshow(Is)

    plt.xlabel('Imagen Original UwU')

    #Imagen convolucionada
    plt.subplot(2,2,2)

    plt.imshow(J)

    plt.xlabel('Imagen con Sharpen OuO')

    #Imprime las imagenes
    plt.grid(False)
    
    plt.show()
