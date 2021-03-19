def MaxPoolingDos(Img):
    fr=len(Img)//2
    cr=len(Img[0])//2
    Resultado=np.zeros((fr,cr),np.uint8)
    

    #Proceso del maxPooling
    a=0
    b=0
    for i in range3(0,len(Img),2):
        for j in range3(0,len(Img),2):
           np.amax(I[a:i+1,b:j+1])
            b=j+1
            a=i+1



