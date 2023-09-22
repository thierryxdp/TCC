def media_matriz(matriz):
    lista = []
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            lista.append(matriz[i][j])
    for l in range(len(lista)):
        total += lista[l]
    return round(total / len(lista), 2)