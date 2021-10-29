import Convolucion_Sharpen as cs
import EdgeDetection1 as ed1
import EdgeDetection3 as ed3
import GaussianBlur as gb
import boxblur as bb

cs.sharpen('hr.png')
ed1.edgeDet1('hr.png')
ed3.edgeDetection3('hr.png')
gb.gaussianBlur('hr.png')
bb.padding_boxblur('hr.png')
