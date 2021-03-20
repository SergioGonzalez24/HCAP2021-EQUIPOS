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

#Imagen 2 003GS.jpeg

#funcion de convolucion con Kn
print("\n")
print("___________________________","\n","Imagen 1 003.jpeg Kernel 1")


print(Img.shape,"\n")
IGS=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

R2Conv1 = convolucion(IGS,Kn)
print(R2Conv2)
print(R2Conv2.shape,"\n")
cv2.imwrite('003C1.jpeg',R2Conv2)

ImgC_2_1 = cv2.imread('002C1.jpeg')
R1Max1 = MaxPoolingDos(ImgC_2_1)
print(R2Max1.shape,"\n")

R2Conv2 = convolucion(R2Max2,Kn)
print(R2Conv2,R2Conv2.shape, sep = "\n")
cv2.imwrite('003C2.jpeg',R2Conv2)

ImgC_2_2 = cv2.imread('003C2.jpeg')
R2Max2 = MaxPoolingDos(ImgC_2_2)
print(R2Max2.shape,"\n")

#funcion de convolucion con In

print("\n")
print("___________________________","\n","Imagen 1 003.jpeg Kernel 2")

print(Img.shape,"\n")
IGS=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

R2Conv2 = convolucion(IGS,In)
print(R2Conv2)
print(R2Conv2.shape,"\n")
cv2.imwrite('003C1.jpeg',R2Conv2)

ImgC_2_1 = cv2.imread('003C1.jpeg')
R2Max2 = MaxPoolingDos(ImgC_2_1)
print(R2Max2.shape,"\n")

R2Conv2 = convolucion(R2Max2,In)
print(R2Conv1,R2Conv2.shape, sep = "\n")
cv2.imwrite('003C2.jpeg',R2Conv2)

ImgC_2_2 = cv2.imread('003C2.jpeg')
R2Max2 = MaxPoolingDos(ImgC_2_2)
print(R2Max2.shape,"\n")

#Imagen 3 008GS.jpeg

#funcion de convolucion con Kn
print("\n")
print("___________________________","\n","Imagen 1 008.jpeg Kernel 1")


print(Img.shape,"\n")
IGS=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

R3Conv1 = convolucion(IGS,Kn)
print(R3Conv1)
print(R3Conv1.shape,"\n")
cv2.imwrite('002C1.jpeg',R3Conv1)

ImgC_3_1 = cv2.imread('008C1.jpeg')
R3Max1 = MaxPoolingDos(ImgC_3_1)
print(R3Max1.shape,"\n")

R3Conv2 = convolucion(R3Max1,Kn)
print(R3Conv2,R3Conv2.shape, sep = "\n")
cv2.imwrite('002C2.jpeg',R3Conv2)

ImgC_3_2 = cv2.imread('008C2.jpeg')
R3Max2 = MaxPoolingDos(ImgC_3_2)
print(R3Max2.shape,"\n")

#funcion de convolucion con In

print("\n")
print("___________________________","\n","Imagen 1 008.jpeg Kernel 2")

print(Img.shape,"\n")
IGS=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

R3Conv1 = convolucion(IGS,In)
print(R3Conv1)
print(R3Conv1.shape,"\n")
cv2.imwrite('002C1.jpeg',R3Conv1)

ImgC_3_1 = cv2.imread('008C1.jpeg')
R3Max1 = MaxPoolingDos(ImgC_3_1)
print(R3Max1.shape,"\n")

R3Conv2 = convolucion(R3Max1,In)
print(R3Conv2,R3Conv2.shape, sep = "\n")
cv2.imwrite('002C2.jpeg',R3Conv2)

ImgC_3_2 = cv2.imread('008C2.jpeg')
R3Max2 = MaxPoolingDos(ImgC_3_2)
print(R3Max2.shape,"\n")

#Imagen 4 011GS.jpeg

#funcion de convolucion con Kn
print("\n")
print("___________________________","\n","Imagen 4 011.jpeg Kernel 1")


print(Img.shape,"\n")
IGS=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

R4Conv1 = convolucion(IGS,Kn)
print(R4Conv1)
print(R4Conv1.shape,"\n")
cv2.imwrite('011C1.jpeg',R4Conv1)

ImgC_4_1 = cv2.imread('011C1.jpeg')
R4Max1 = MaxPoolingDos(ImgC_4_1)
print(R4Max1.shape,"\n")

R4Conv2 = convolucion(R4Max1,Kn)
print(R4Conv2,R4Conv2.shape, sep = "\n")
cv2.imwrite('002C2.jpeg',R4Conv2)

ImgC_4_2 = cv2.imread('011C2.jpeg')
R4Max2 = MaxPoolingDos(ImgC_4_2)
print(R4Max2.shape,"\n")

#funcion de convolucion con In

print("\n")
print("___________________________","\n","Imagen 4 011.jpeg Kernel 2")

print(Img.shape,"\n")
IGS=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

R4Conv1 = convolucion(IGS,In)
print(R4Conv1)
print(R4Conv1.shape,"\n")
cv2.imwrite('011C1.jpeg',R4Conv1)

ImgC_4_1 = cv2.imread('011C1.jpeg')
R4Max1 = MaxPoolingDos(ImgC_4_1)
print(R4Max1.shape,"\n")

R4Conv2 = convolucion(R4Max1,In)
print(R4Conv2,R4Conv2.shape, sep = "\n")
cv2.imwrite('011C2.jpeg',R4Conv2)

ImgC_4_2 = cv2.imread('011C2.jpeg')
R4Max2 = MaxPoolingDos(ImgC_4_2)
print(R4Max2.shape,"\n")
