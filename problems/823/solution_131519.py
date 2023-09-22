def faltante(L):
    """função que, dada uma lista com números inteiros numerados, retorna
    o número inteiro deste intervalo que está faltando.

    list -> int

    exemplos:
    faltante([1,2,4])==3
    faltante([1,2,3,4,5,7,8])==6
    faltante([1,2,3,4])==5"""
    i=0
    L.sort()
    while i != len(L)
        L[i]==i+1
        i=i+1
    return L[i]+1