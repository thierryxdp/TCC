def faltante(lista):
    '''Funcao que dada uma lista com N-1 inteiros numerados de 1 a N,
    retorna qual numero inteiro deste intervalo esta faltando
    list -> int'''
    elemento = 1
    posicao = 1 
    while posicao<len(lista):
        if (elemento + 1) < lista[posicao]: 
            elemento = elemento + 1
            return elemento
        else:
            elemento = lista[posicao]
            posicao = posicao + 1
    return posicao + 1