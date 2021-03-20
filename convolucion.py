import numpy as np
import cv2


def convolucion(original,Kernel):
    fr=len(original)-(len(Kernel)-1)
    cr=len(original[0])-(len(Kernel[0])-1)
    Resultado=np.zeros((fr,cr),np.uint8)
    #For para recorrer filas
    for i in range(len(Resultado)):
        #For para recorrer columnas
        for j in range(len(Resultado[0])):
            suma=0
            #hace las multiplicaciones y las suma
            for m in range(len(Kernel)):
                for n in range(len(Kernel[0])):
                    suma+=Kernel[m][n]*original[m+i][n+j]
            if suma<=255:        
                Resultado[i][j]=round(suma)
            else:
                Resultado[i][j]=255
    return Resultado


from MaxPooling import maxpoolGlobal

'''
#imagenes
K=[[-1,0,1],[-1,0,1],[-1,0,1]]
I=[[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]
'''
#imagenes a numpy arrays
In = np.array([[2,2,4,2,2],[1,1,2,1,1],[0,0,0,0,0],[-1,-1,-2,-1,-1],[-2,-2,-4,-2,-2]])
Kn = 1/256*np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,2,1]])
'''
IRGB=cv2.imread('002.jpeg')
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS.shape)
'''
#funcion de convolucion
R1 = maxpoolGlobal(2)
print(R1.shape)
R=convolucion(R1,Kn)
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

