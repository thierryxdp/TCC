def faltante(L):
    """função recebe uma PA de razão 1, sem um elemento e retorna esse elemento faltante. LIST(INT)->INT"""
    Lideal=[]
    i=0
    j=1
    k=0
    somareal=0
    somaideal=0
    while i<len(L):
        somareal=somareal+L[i]
        i=i+1
    while j<len(L)+1:
        j=j+1
        Lideal.append(j)
    while k<len(Lideal):
        somaideal=somaideal+Lideal[k]
        k=k+1
    x=somaideal-somareal+1
    return x