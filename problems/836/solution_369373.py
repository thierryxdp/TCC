def busca(palavra, matriz):
    matriz=[]
    i=0
    for  i in range(len(matriz)):
        if palavra.lower( ) in matriz[i][0].lower( ):
            matriz.append(matriz[i])
            i=i+1
        else:
                i=i+1
    return matriz