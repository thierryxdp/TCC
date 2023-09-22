def eh_quadrada(matriz):
    contlin=0
    contcol=0
    for i in matriz:
        contlin+=1
        for j in i:
            contcol+=1
    if contlin!=contcol:
        return False