def faltante(L):
    '''Funcao que, dada uma lista (L) com N-1 inteiros numerados de 1 a N, retorna o numero que está faltando; list[int,...] -> int'''
    list.sort(L)
    n=0
    if L[0]!=1:
        return 1
    while n<len(L)-1:
        if L[n]==L[n+1]-1:
            n+=1
        else:
            return L[n]+1
    else:
        return len(L)+1