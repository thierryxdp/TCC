def faltante(L):
    posicao = i 
    i=0
    n = 1
    while i < len(L) + 1:
        if L[posicao] != n:
            return n
        else:
            i = i+1
            n = n+1
            posicao += 1