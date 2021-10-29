import numpy
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

#Convolucion boxblur 1/9[karnel]
def boxblur(img):
    Is = Image.open(img)
    #Convertir en escala de grises
    I = Is.convert('L')
    #Conversion numerica para poder operar de 0-1
    I = numpy.asarray(I)
    #Normalizacion 0 - 1
    I = I / 255.0
    
    #Dar los valores de karnel
    k_sharen = numpy.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
    '''
         | 1  1  1 |
    (1/9)| 1  1  1 |
         | 1  1  1 |
    '''
    
    J = ndimage.convolve(I, k_sharen, mode='constant', cval=0.0)

    #Tamanio de la imagen
    plt.figure(figsize = (20,20))
    
    #Imagen original
    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    #Imagen Con padding
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
    Is = Image.open(img);
    #Convertir en escala de grises
    I = Is.convert('L');
    #Conversion numerica para poder operar de 0-1
    I = numpy.asarray(I);
    #Normalizacion 0 - 1
    I = I / 255.0;
    
    #Utilizar la funcion de padding 
    I = numpy.pad(I, 10, pad_with, padder=0)
    
    #Dar los valores de karnel
    k_sharen = numpy.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
    '''
         | 1  1  1 |
    (1/9)| 1  1  1 |
         | 1  1  1 |
    '''
    
    J = ndimage.convolve(I, k_sharen, mode='constant', cval=0.0)
    
    #Tamanio de la imagen
    plt.figure(figsize = (20,20))
    
    #Imagen original
    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    #Imagen Con padding
    plt.subplot(2,2,2)
    plt.imshow(J)
    plt.xlabel('Padding Box Blur')

    plt.grid(False)
    plt.show()
