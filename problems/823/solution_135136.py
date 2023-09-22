def faltante(pecas):
    '''recebe uma lista com N − 1 inteiros numerados de 1 a N e descubra qual número inteiro deste intervalo está faltando'''
    '''list -> int'''
    list.sort(pecas)
    if pecas[0] != 1:
        return 1