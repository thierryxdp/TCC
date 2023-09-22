def busca(palavra, matriz):
    matriz=[]
    i=0
    for  i in range(len(matriz)):
        if palavra.lower( ) in lista[i][0].lower( ):
            matriz.append(lista[i])
            i=i+1
        else:
                i=i+1
    return matriz