def faltante(L):
    'função que recebe lista com números inteiros e sequenciais retornando'
    'qual está faltando'
    list.sort(L)
    x=L[0]
    n=L[0]
    y=0
    while L[y]<len(L):
        if L[x]==n:
            n+=1
            x+=1
        else:
            return x+1