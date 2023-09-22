def media_matriz(matriz):
    '''dado uma matriz de inteiros, retorna a media de todos os elementos dessa matriz.
    list -> float'''
    n = 0
    soma = 0 
    elementos = 0
    i = 0
    while i < len(matriz):
        c = sum(matriz[n])
        soma = soma + c
        d = len (matriz[n])
        n = n + 1
        elementos = elementos + d
        i = i + 1
    return soma/elementos