def filtraMultiplos(lista_orig, num):
    multiplos = []
    cont = 0
    while lista_orig[cont] % num == 0:
        multiplos.append(lista_orig[cont])
        cont += 1
	return multiplos