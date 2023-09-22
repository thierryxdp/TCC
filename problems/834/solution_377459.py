def media_matriz(matriz):
    '''Retorna a media de todos os numeros da matriz
    de entrada(composta apenas por inteiros) com duas
    casas de precisao
    list -> float'''
    soma = 0
    quantidade = 0
    for linha in matriz:
        for elemento in linha:
            soma = soma + elemento
            quantidade += 1
    media = soma/quantidade
    return round(media,2)