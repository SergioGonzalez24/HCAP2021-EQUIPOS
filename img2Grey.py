import cv2
import numpy as np

def img2Grey(original,nombre):

    IRGB= cv2.imread(original)
    print(IRGB)
    print(IRGB.shape)
    print("Lineas agregadas en la rama2")
    IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
    print(IGS)
    print(IGS.shape)
    return cv2.imwrite(nombre,IGS)




img2Grey("002.jpeg","002GS.jpeg")
img2Grey("003.jpeg","003GS.jpeg")
img2Grey("008.jpeg","008GS.jpeg")
img2Grey("011.jpeg","011GS.jpeg")

