def faltante(lista_pecas):
    '''Uma função que, dada uma lista com N − 1 inteiros 
    numerados de 1 a N, descubre qual número
    inteiro deste intervalo está faltando list[int]->int.'''
    i = len(lista_pecas) + 1
    somafinal = i * (i + 1) // 2
    return somafinal - sum(lista_pecas)