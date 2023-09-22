def filtraMultiplos(lista, numero):
    contador = 0
    nova_lista = []
    while contador <= len(lista):
        if lista[contador]%numero == 0:
            list.append(nova_lista, lista[contador])
		contador = contador + 1
    return nova_lista