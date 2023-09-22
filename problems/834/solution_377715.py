def media_matriz(matriz):
    ''' função que recebe uma matriz de inteiros não vazia e retorna a média de todos os seus números;
    list -> float '''
    media = 0
    for i in matriz:
        for numero in i:
            media = media + numero
        resultado = media/(len(matriz)*len(matriz[0]))
    return round(resultado, 2)