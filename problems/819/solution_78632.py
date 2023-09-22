def filtraMultiplos(lista, n):
    tamanho = len(lista)
    acumulador = []
    i = 0
    while i < tamanho:
        if lista[i]%n == 0:
            acumulador.append(lista[i])
	return lista