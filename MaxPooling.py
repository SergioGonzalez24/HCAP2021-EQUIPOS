import numpy as np
import cv2
#def maxpoolGlobal(res):

def MaxPoolingDos(Img):
    fr=len(Img)//2
    cr=len(Img[0])//2
    Resultado=np.zeros((fr,cr),np.uint8)
    

    #Proceso del maxPooling
    a=0
    for i in range(0,len(Img),2):
        b=0
        for j in range(0,len(Img),2):
            Resultado[a][b]=np.amax(Img[i:i+2,j:j+2])
            b+=1
        a+=1
    return Resultado

