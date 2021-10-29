'''
Juan Carlos Varela Tellez      A01367002
Ximena Valeria Cabanas Sanchez A01366707
Tomas Ulises Pena Martinez     A01366603
Keyuan Zhao                    A01366831
Alan Eduardo Aquino Rosas      A01366912
'''


#Importacion de programas
import Convolucion_Sharpen as cs #Valeria
import EdgeDetection1 as ed1     #Juan 
import edgeDetection2 as ed2     #Tomas (bonus)
import EdgeDetection3 as ed3     #Alan
import GaussianBlur as gb        #Tomas
import boxblur as bb             #Keyuan

#Ejecucion de funciones
cs.sharpen('hr.png')
ed1.edgeDet1('hr.png')
ed2.edgeDetection2('hr.png')
ed3.edgeDetection3('hr.png')
gb.gaussianBlur('hr.png')
bb.padding_boxblur('hr.png')
