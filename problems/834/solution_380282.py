def media_matriz(media):
    '''Função que dada uma matriz de inteiros não vazia, retorne a média de todos os números da matriz, int -> int, float'''
    x = 0
    y = 0
    for i in media:
        x = sum(i) + x
        for j in media:
            y = len(j) + y
    return x / y