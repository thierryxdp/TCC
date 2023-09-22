def media_matriz(matriz):
    lista = []
    for i in matriz:
        for j in i:
            lista.append(j)
    return round(sum(lista) / len(lista), 2)