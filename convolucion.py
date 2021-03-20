import numpy as np
import cv2
from MaxPooling import MaxPoolingDos
#from MaxPooling import maxpoolGlobal


def convolucion(Ioriginal,Kernel):
    fr=len(Ioriginal)-(len(Kernel)-1)
    cr=len(Ioriginal[0])-(len(Kernel[0])-1)
    Resultado=np.zeros((fr,cr),np.uint8)
    #For para recorrer filas
    for i in range(len(Resultado)):
        #For para recorrer columnas
        for j in range(len(Resultado[0])):
            suma=0

            #hace las multiplicaciones y las suma
            for m in range(len(Kernel)):
                for n in range(len(Kernel[0])):
                    suma+=Kernel[m][n]*Ioriginal[m+i][n+j]
            if suma<=255:        
                Resultado[i][j]=round(suma)
            else:
                Resultado[i][j]=255
    return Resultado




#imagenes a numpy arrays
In = np.array([[2,2,4,2,2],[1,1,2,1,1],[0,0,0,0,0],[-1,-1,-2,-1,-1],[-2,-2,-4,-2,-2]])
Kn = 1/256*np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,2,1]])

Img=cv2.imread('002.jpeg')
Img2=cv2.imread('003.jpeg')
Img3=cv2.imread('008.jpeg')
Img4=cv2.imread('011.jpeg')

#funcion de convolucion con Kn

#Imagen 1 002GS.jpeg

print(Img.shape,"\n")
IGS=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

R1Conv1 = convolucion(IGS,Kn)
print(R1Conv1)
print(R1Conv1.shape,"\n")
cv2.imwrite('002C.jpeg',R1Conv1)

R1Max1 = MaxPoolingDos("002C.jpeg")
print(R1Max1.shape,"\n")

R1Conv2 = convolucion(R1Max1,Kn)
print(R1Conv2,R1Conv2.shape, sep = "\n")
cv2.imwrite('002C.jpeg',R1Conv2)

R1Max2 = MaxPoolingDos("002C.jpeg")
print(R1Max2.shape,"\n")

'''


IRGB=cv2.imread('002.jpeg')
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS.shape)

#funcion de convolucion
R=convolucion(IGS,Kn)
print(R)
print(R.shape)
cv2.imwrite('002C.jpg',R)






R2= maxpoolGlobal(2)
R=convolucion(R2,Kn)
print(R)
print(R.shape)
cv2.imwrite('003C.jpg',R)

R3 = maxpoolGlobal(2)
R=convolucion(R3,Kn)
print(R)
print(R.shape)
cv2.imwrite('008C.jpg',R)

R4 = maxpoolGlobal(2)
R=convolucion(R4,Kn)
print(R)
print(R.shape)
cv2.imwrite('011C.jpg',R)
#HOLA TEAM         

'''
