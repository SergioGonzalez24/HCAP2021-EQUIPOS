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



#Imagen 1 002GS.jpeg

#funcion de convolucion con Kn
print("\n")
print("___________________________","\n","Imagen 1 002.jpeg Kernel 1")


print(Img.shape,"\n")
IGS=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

R1Conv1 = convolucion(IGS,Kn)
print(R1Conv1)
print(R1Conv1.shape,"\n")
cv2.imwrite('002C1.jpeg',R1Conv1)

ImgC_1_1 = cv2.imread('002C1.jpeg')
R1Max1 = MaxPoolingDos(ImgC_1_1)
print(R1Max1.shape,"\n")

R1Conv2 = convolucion(R1Max1,Kn)
print(R1Conv2,R1Conv2.shape, sep = "\n")
cv2.imwrite('002C2.jpeg',R1Conv2)

ImgC_1_2 = cv2.imread('002C2.jpeg')
R1Max2 = MaxPoolingDos(ImgC_1_2)
print(R1Max2.shape,"\n")

#funcion de convolucion con In

print("\n")
print("___________________________","\n","Imagen 1 002.jpeg Kernel 2")

print(Img.shape,"\n")
IGS=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

R1Conv1 = convolucion(IGS,In)
print(R1Conv1)
print(R1Conv1.shape,"\n")
cv2.imwrite('002C1.jpeg',R1Conv1)

ImgC_1_1 = cv2.imread('002C1.jpeg')
R1Max1 = MaxPoolingDos(ImgC_1_1)
print(R1Max1.shape,"\n")

R1Conv2 = convolucion(R1Max1,In)
print(R1Conv2,R1Conv2.shape, sep = "\n")
cv2.imwrite('002C2.jpeg',R1Conv2)

ImgC_1_2 = cv2.imread('002C2.jpeg')
R1Max2 = MaxPoolingDos(ImgC_1_2)
print(R1Max2.shape,"\n")