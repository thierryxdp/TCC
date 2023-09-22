def media_matriz(matriz):
    """A função retorna a média dos elementos de uma matriz
    list-->float"""
    
    soma = 0
    i = 0
    for lista in matriz:
        for item in lista:
            soma += item
            i += 1
    media = soma/i
    return round(media,2)