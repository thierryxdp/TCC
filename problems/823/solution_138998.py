def faltante(L):
    cont = 0
    N = 1
    faltou = len(L) + 1
    while cont < len(L):
        if L[cont] != N:
            faltou = N
            break
        N += 1
        cont += 1
	return faltou