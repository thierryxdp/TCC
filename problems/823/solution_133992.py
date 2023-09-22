def faltante(L):
    '''Função que, dada uma lista L contendo N-1 números inteiros numerados de 1 até N, descobre qual número deste intervalo está faltando.
list --> int'''
    i = 0
    list.sort(L)
    list.append(L,L[-1]+2)
    if 1 not in L:
        return 1
    while i < len(L):
        if L[i] == L[i+1]-2:
            return L[i]+1
        i = i+1