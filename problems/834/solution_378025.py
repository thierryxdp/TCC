def media_matriz(matriz):
    '''Programa que retorna a media da soma da matriz de entrada
    list -> float'''
    ln = len(matriz)
    lm = len(matriz[0])
    i = 0
    l = []
    for i in range(len(matriz)):
        soma = sum(matriz[i])
        div = soma/lm
        list.append(l, div)
    som = sum(l)
    return round(som/ln,2)