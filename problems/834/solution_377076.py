def media_matriz(matriz):
    '''Funcao que recebe uma matriz de inteiros, nao vazia, e retorna a media
    de todos os numeros dela'''
    med = 0
    for linha in matriz:
        for elemento in linha:
            med = med + elemento
        conta = med/(len(matriz)*len(matriz[0]))
    return round(conta,2)