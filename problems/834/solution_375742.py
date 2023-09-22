def media_matriz(matriz):

    lista = []

    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            lista.append(matriz[l][c])

    return round(sum(lista)/len(lista), 2)