def media_matriz(media):
    '''Função que dada uma matriz de inteiros não vazia, retorne a média de todos os números da matriz, int -> int, float'''
    x = 0
    y = 0
    for i in range(len(media)):
        x = sum(i) + x
        for j in range(len(media)):
            y = len(j) + y
    return round(media, 2)