def eh_quadrada(matriz):
    contlin=0
    contcol=0
    for i in range(len(matriz)):
        contlin+=1
        for j in range(0,i):
            contcol+=1
    if contlin==contcol:
        return True
    if contlin==0:
        return True
    elif contlin!=contcol:
        return False