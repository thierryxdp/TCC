def faltante (L):
    """descobre qual peça do quebra cabeça está faltando"""
    list.sort(L)
    i=0
    numero=L[i]
    while i<len(L) and i+1==numero:
        i=i+1
        numero=L[i]
        return i