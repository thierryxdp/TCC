def faltante(L):
    """A funcao recebe umalista e avalia dentro do intervalo qual a peça esta faltando. Depois retorna o numero.
    list ->int"""
    L.sort()
    i=1
    if L[0] !=1:
        return 1
    while i<len(L):
        if (L[i]-L[i-1]) !=1:
            return int((L[i]+L[i-1])/2)
        i=i+1
    if L[0]==1:
        return L[-1]+1