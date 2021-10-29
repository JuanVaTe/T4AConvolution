import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

def pad_width(vector,pad_width,iaxis,kwargs):
    pad_value=kwargs.get('padder',10)
    vector[:pad_width[0]]=pad_value
    vector[-pad_width[1]:]=pad_value


def edgeDetection3(imageDetection):
   Is=Image.open(imageDetection)
   I=Is.convert('L')
   I=numpy.asarray(I)
   I=I/255.0
   I=numpy.pad(I,30,pad_width,padder=1)

   k=numpy.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

   J=ndimage.convolve(I,k,mode='constant',cval=0.0)

   plt.figure(figsize=(15,15))

   plt.subplot(2,2,1)
   plt.imshow(Is)
   plt.xlabel('Imagen original')

   plt.subplot(2,2,2)
   plt.imshow(J)
   plt.xlabel('Edge Detection 3')


   plt.grid(False)
   plt.show()









