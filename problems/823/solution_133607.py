def faltante(lista):
    '''função que, dada uma lista com N − 1 inteiros numerados de 1 a N, descubra qual número
inteiro deste intervalo está faltando; list->int'''
    lista.sort()
    ind=1
    while ind in lista:
        ind=ind+1
    return ind