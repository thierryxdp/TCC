def media_matriz(matriz):
    '''Funcao que calcula e retorna a media de todos os
    numeros da matrizm, com duas casas de precisao
    list(list) -> float'''
    s = 0
    t = 0
    for linha in matriz:
        s = s + sum(linha)
        t = t + len(linha)
    media = s/t
    return round(media,2)