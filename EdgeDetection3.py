import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage
#Funcion de padding 
def pad_width(vector,pad_width,iaxis,kwargs):
    pad_value=kwargs.get('padder',10)
    vector[:pad_width[0]]=pad_value
    vector[-pad_width[1]:]=pad_value

 #Se recive como parametro el nombre de la imagen
def edgeDetection3(imageDetection):
    #Se abre la imagen y se convierte a la matriz
   Is=Image.open(imageDetection)
   I=Is.convert('L')
   I=numpy.asarray(I)
   I=I/255.0
   I=numpy.pad(I,30,pad_width,padder=1)
     #El kernel o filto que se esta ocupando:Edge Detection 3 
   k=numpy.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    #Se realiza la convolucion con el kernel correspondiente 
   J=ndimage.convolve(I,k,mode='constant',cval=0.0)

   plt.figure(figsize=(15,15))
 #Plot imagen original
   plt.subplot(2,2,1)
   plt.imshow(Is)
   plt.xlabel('Imagen original')
#Plot imagen con convolusion
   plt.subplot(2,2,2)
   plt.imshow(J)
   plt.xlabel('Edge Detection 3')


   plt.grid(False)
   plt.show()









