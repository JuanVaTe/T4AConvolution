'''
Juan Carlos Varela Tellez      A01367002
Ximena Valeria Cabanas Sanchez A01366707
Tomas Ulises Pena Martinez     A01366603
Keyuan Zhao                    A01366831
Alan Eduardo Aquino Rosas      A01366912
'''


#Importacion de programas
import sys
import Convolucion_Sharpen as cs #Valeria
import EdgeDetection1 as ed1     #Juan 
import edgeDetection2 as ed2     #Tomas (bonus)
import EdgeDetection3 as ed3     #Alan
import GaussianBlur as gb        #Tomas
import boxblur as bb             #Keyuan

#Obtencion del argumento
arg = int(sys.argv[1])

#Ejecucion de funciones
if arg == 1:
    cs.sharpen('hr.png')
if arg == 2:
    ed1.edgeDet1('hr.png')
if arg == 3:
    ed2.edgeDetection2('hr.png')
if arg == 4:
    ed3.edgeDetection3('hr.png')
if arg == 5:
    gb.gaussianBlur('hr.png')
if arg == 6:
    bb.padding_boxblur('hr.png')
