def eh_quadrada(matriz):
    contlin=0
    contcol=0
    for i in range(0,len(matriz)):
        contlin+=1
        for j in range(0,i+1):
            contcol+=1
    if contlin==contcol:
        return True
    if contlin==0:
        return True
    elif contlin!=contcol:
        return False