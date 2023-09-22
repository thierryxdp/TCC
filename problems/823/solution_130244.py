def faltante(L):
    tamanhoL = len(L) + 1
    posicao = i = x = 0
    n = 1
    while i < tamanhoL:
        if L[posicao] == n:
            x = L[posicao]
        else:
            i += 1
 	return x