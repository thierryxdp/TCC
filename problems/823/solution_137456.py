def faltante(lista):
    '''dada uma lista com (N-1) inteiros numerados de 1 a N , retorna qual número
    inteiro deste intervalo está faltando;
    list -> int'''
    peca = 1

    while peca in lista:
        peca += 1

    return peca