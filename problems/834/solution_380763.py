def media_matriz(matriz):
    lista = []
    for c in range(len(matriz)):
        for i in range(len(matriz[c])):
            lista.append(matriz[c][i])
    return round(sum(lista)/len(lista),2)