def faltante (L):
    """descobre qual peça do quebra cabeça está faltando"""
    list.sort(L)
    i=0
    while i<len(L) and i==int(L[i]):
        i=i+1
        return i