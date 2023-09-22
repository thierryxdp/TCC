def faltante(L):
    i = 0
    peca = 1
    list.sort(L)
    while i<len(L):
        if peca == L[i]:
            peca +=1
        i += 1
    return peca