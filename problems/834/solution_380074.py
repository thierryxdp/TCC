def media_matriz(matriz):
    """A função retorna a média dos elementos de uma matriz
    list-->float"""
    
    soma = 0
    i = 0
    media = soma/i
    for lista in matriz:
        for item in lista:
            soma += item
            i += 1
    return round(media,2)