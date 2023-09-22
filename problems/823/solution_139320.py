def faltante1(L):
    'função que recebe lista com números inteiros e sequenciais retornando'
    'qual está faltando'
    list.sort(L)
    x=1
    y=0
    while L[y]<len(L):
        if L[y]==x:
            y+=1
            x+=1
        else:
            y+=1
    return x