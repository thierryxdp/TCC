def media_matriz(matriz):
    lista=[]
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
             lista.append(matriz[i][j])
    for x in range(len(lista)):
        soma+=lista[i]
    return soma/len(lista)