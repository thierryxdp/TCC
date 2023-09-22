def faltante (L):
    """descobre qual peça do quebra cabeça está faltando"""
    L=list.sort(L)
    i=0
    while i<len(L):
        if L[i]==str(L[i]):
        i=i+1
        return i