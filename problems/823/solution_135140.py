def faltante(pecas):
    '''recebe uma lista com N − 1 inteiros numerados de 1 a N e descubra qual número inteiro deste intervalo está faltando'''
    '''list -> int'''
    i = 0
    repete  =  0
    while i < len(lista):
        se  lista [i] == lista [i - 1]:
            repete = repete + 1
        i= i+1
    return repete