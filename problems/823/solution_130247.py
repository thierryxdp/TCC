def faltante(L):
    tamanhoL = len(L) + 1
    posicao = i = x = 0
    n = 1
    while i < tamanhoL:
        if L[posicao] != n:
            return n
        else:
     		i += 1
          	n += 1