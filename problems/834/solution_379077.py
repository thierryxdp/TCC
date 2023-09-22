def media_matriz(matriz):
    lista = []
    for x in matriz:
        for y in x:
            lista.append(y)
    return round(sum(lista)/len(lista), 2)