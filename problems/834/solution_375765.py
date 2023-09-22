def media_matriz(matriz):
    '''dada uma matriz, retorna a media de seus elementos com 2 casas decimais de precisao
    list -> float'''
    soma = 0
    cont = 0
    for linha in matriz:
        for item in linha:
            soma += item
            cont += 1
    media = soma/cont
    return round(media, 2)