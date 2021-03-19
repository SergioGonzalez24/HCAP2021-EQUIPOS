import numpy as np
import cv2
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
Img=cv2.imread('002GS.jpeg')
Img2=cv2.imread('003GS.jpeg')
Img3=cv2.imread('008GS.jpeg')
Img4=cv2.imread('011GS.jpeg')
R1=MaxPoolingDos(Img)
R2=MaxPoolingDos(Img2)
R3=MaxPoolingDos(Img3)
R4=MaxPoolingDos(Img4)
print(R1)
print(R2)
print(R3)
print(R4)

