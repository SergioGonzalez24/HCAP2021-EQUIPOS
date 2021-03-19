import cv2
import numpy as np

#Cargar la imagen a color
IRGB_1 = cv2.imread('002.jpg')
IGRGB_2 = cv2.imread("003.jpg")
IRGB_3 = cv2.imread("008.jpg")
IRGB_4 = cv2.imread("011.jpg")

def img2Grey(imagen,nombreArchvioGrey):

    print(imagen)
    print(imagen.shape)
    print("Lineas agregadas en la rama2")
    IGS=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    print(IGS)
    print(IGS.shape)
    cv2.imwrite(NombreArchivoGrey,IGS)


img2Grey(IRGB_1,"002GS.jpg")
img2Grey(IGRGB_2,"003GS.jpg")
img2Grey(IRGB_3,"008GS.jpg")
img2Grey(IRGB_4,"011GS.jpg")


