def faltante(L):
    'função que recebe lista com números inteiros e sequenciais retornando'
    'qual está faltando'
    list.sort(L)
    x=0
    n=0
    while L[x]<len(L):
        if L[x]==n:
            n+=1
            x+=1
        else:
            return x