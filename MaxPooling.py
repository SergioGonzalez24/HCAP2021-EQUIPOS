def MaxPoolingDos(Img):
    fr=len(Img)//2
    cr=len(Img[0])//2
    Resultado=np.zeros((fr,cr),np.uint8)
    
    #Proceso del maxPooling
