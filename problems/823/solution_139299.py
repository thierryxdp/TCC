def faltante (L):
    """descobre qual peça do quebra cabeça está faltando"""
    list.sort(L)
    i=0
    numero=L[i]
    N=len(L)+1
    while i<N and i+1==numero:
        i=i+1
        numero=L[i+1]
    return i