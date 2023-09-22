def faltante(L):
    lista_certa = []
    N = len(L) + 1
    cont = 1
    while cont <= N:
        lista_certa += [cont,]
        cont += 1
	cont = 0
    while cont <= N:
        if L[cont] != lista_certa[cont]:
            faltou = lista_certa[cont]
	return faltou