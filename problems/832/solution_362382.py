def eh_quadrada(matriz):
    contlin=0
    contcol=0
    for i in range(len(matriz)):
        contlin+=1
        for j in range(i):
            contcol+=1
    if contlin==contcol or len(matriz)=0:
        return True
    else:
        return False