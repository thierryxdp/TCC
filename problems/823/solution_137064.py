def faltante(L:list)->int:
    """função que descubra qual número inteiro do intervalo da lista está faltando"""
    i=0
    while len(L)<i:
        if not L[i]+1 in L:
            falt=L[i]+1
        i-=1
    return falt