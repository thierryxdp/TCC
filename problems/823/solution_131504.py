def faltante(L):
    """função que, dada uma lista com números inteiros numerados, retorna
    o número inteiro deste intervalo que está faltando.

    list -> int

    exemplos:
    faltante([1,2,4])==3
    faltante([7,6,4,3])==5
    faltante([9,8,7,5])==6"""
    i=0
    if L[-1]>L[-2]:
        while L[i+1]-L[i]==1:
            i=i+1
        return L[i]+1
    if L[-1]<L[-2]:
        while L[i+1]-L[i]==-1:
            i=i+1
        return L[i]-1