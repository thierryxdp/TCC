def elementos_matriz(matriz, i, j):
    return matriz[i][j]

def media_matriz(matriz):
    lista = list(map(elementos_matriz, len(matriz), len(matriz[0])))
    return round((sum(lista)/len(lista)), 2)