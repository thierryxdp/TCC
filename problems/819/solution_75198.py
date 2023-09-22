def filtraMultiplos(lista, numero):
    i = 0
    novaLista = []
    while i <= len(lista):
        i += 1
        if lista[i] % numero == 0:
            novaLista.append(lista[i])

        return novaLista