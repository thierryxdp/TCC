def filtraMultiplos(lista, numero):
    nova_lista = ()
    quantidade_repeticoes = len(lista) - 1
    index = 0
    while repetir < quantidade_repeticoes:
        if lista[index] / numero == 0:
            nova_lista = nova_lista + lista[index]
            index = index + 1
	return nova_lista