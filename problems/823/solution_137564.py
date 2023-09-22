def faltante(L):
    '''Função que dada uma lista com N-1 inteiros, pois
existe uma peça faltante, numerada de 1 a N, retorna qual
número deste intervalo está faltando;
	lista -> int'''
    L.sort()
    if 1 not in L:
        return 1
    if L[:-1] < len(L)+1:
        return L[:-1]+1
    proximo=0
    indice=0
    while indice < len(L):
        if L[proximo+1]-L[proximo]!=1:
            indice=indice+1
            proximo=proximo+1
    return L[proximo]+1