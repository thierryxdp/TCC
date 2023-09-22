def faltante(l):
    """
    indica qual peca do quebra cabeca esta faltando
    """
    pecas=list(range(max(l)+1))
    pecas.remove(0)
    i=1
    while i<len(pecas):
        if pecas[i-1] not in l:
            return i
        i+=1