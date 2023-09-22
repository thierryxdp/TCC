def media_matriz(media):
    '''Função que dada uma matriz de inteiros não vazia, retorne a média de todos os números da matriz, int -> int, float'''
    x = 0
    for i in range(len(media)):
        x = sum(i/2)
    return round(x, 2)