def faltante(L):
    '''função que, dada uma lista com N-1 inteiros numerados de 1 a N,
    retorna qual número inteiro (x) deste intervalo está faltando; 
    list -> int'''
    list.sort(L)
    x = 0
    i = 0
    while i < len(L)+1:
        if L[i-1] != L[i]+1:
            x = i + 1
        i = i + 1
    if x < L[0]:
        return x
    else:
        return x+1