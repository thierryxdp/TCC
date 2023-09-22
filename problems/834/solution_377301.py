def media_matriz(matriz):
    """retorna a média de todos os números da matriz.
    list->float"""
    n=0
    soma=0
    for i in range(len(matriz)):
        for j in matriz[i]:
            soma=soma+j
            n=n+1
    media=soma/n
    return round(media,2)