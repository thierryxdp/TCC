def media_matriz(matriz):
    somatorio=0
    cont=0
    cont2=0
    for i in range(len(matriz)):
        cont=cont+1
        for j in range(len(matriz[0])):
            somatorio=somatorio+matriz[i][j]
            cont2=j+1
    x=cont*cont2
    resultado=somatorio/x
    return round(resultado,2)