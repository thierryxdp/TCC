def faltante(L):
    '''Função que dada uma lista de N-1 inteiros numerados de 1 a N, retirna o número inteiro x que pertence ao intervalo[1,N] mas que não pertence a ista de entrada L.'''
    '''list->int'''
    list.sort(L)
    proximo = 1
    if len(L) == L[-1]:
        return L[-1] + 1
    while L[proximo - 1] == proximo :
        proximo = proximo + 1
    return proximo