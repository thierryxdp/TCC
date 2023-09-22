def faltante (L):
    """descobre qual peça do quebra cabeça está faltando"""
    L=list.sort(L)
    i=0
    while i<len(L):
        if i==L[i]:
        i=i+1
        return i