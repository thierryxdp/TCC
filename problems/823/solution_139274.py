def faltante (L):
    """descobre qual peça do quebra cabeça está faltando"""
    list.sort(L)
    i=0
    letra=L[i]
    while i<len(L) and i==letra:
        i=i+1
        return i