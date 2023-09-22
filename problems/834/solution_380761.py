def media_matriz(matriz):
    lista = []
    for c in range(len(matriz)):
        for i in range(len(matriz[c])):
            lista.append(matriz[c][i])
    return sum(lista)/len(lista)