def faltante(lista):
    '''Função que dada uma lista com N-1 inteiros numerados
    de 1 a N, descubra qual o numero inteiro deste intervalo
    esta faltando
    list -> int'''
    i = 0
    s = 0
    n = 0
    soma = (((1+(len(lista)+1))*(len(lista)+1))/2)
    list.sort(lista)
    while i<len(lista):
        if sum(lista) != soma:
            s = (soma)-sum(lista)
        i += 1
        n += 1
    return s