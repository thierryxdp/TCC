def filtraMultiplos(lista, numero)
	i = 0
    novaLista = []
    while i < len(lista):
        if lista[i] % numero == 0:
            novaLista.append(lista[i])

        i += 1

    return novaLista