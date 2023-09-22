def media_matriz(media):
    '''Função que dada uma matriz de inteiros não vazia, retorne a média de todos os números da matriz, int -> int, float'''
    x = 0
    y = 0
    for i in media:
        x = sum(i) + x
        y = len(i) + y
    return round(x / y, 2)