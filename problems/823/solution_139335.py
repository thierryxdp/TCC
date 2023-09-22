def faltante (L):
    """descobre qual peça do quebra cabeça está faltando"""
    list.sort(L)
    i=0
    numero=L[i]+1
    Npecas=len(L)+1
    while i+1<Npecas:
        numero=L[i]+1
        i=i+1
    return i