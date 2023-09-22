def faltante(L):
    '''função que, dada uma lista com N-1 inteiros numerados de 1 a N,
    retorna qual número inteiro deste intervalo está faltando; 
    list -> int'''
    list.sort(L)
    i = 0
    while i < len(L)+1:
        if i+1 not in L:
            return i+1
        if L[i] != i+1:
            return i+1
        i = i + 1