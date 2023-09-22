def soma(matriz, i):
    return sum(matriz)

def media_matriz(matriz):
    lista = list(map(soma, matriz, range(len(matriz))))
    return round((sum(lista)/(len(lista)*len(matriz[0]))), 2)