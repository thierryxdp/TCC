def eh_quadrada(matriz):
    contlin=0
    contcol=0
    for i in matriz:
        contlin+=1
        for j in i:
            contcol+=1
    if contlin==contcol:
        return True
    if contlin==0:
        return True
    else:
        return False