def filtraMultiplos(lista, numero):
    nova_lista = []
    quantidade_repeticoes = len(lista) - 1
    index = 0
    while index < quantidade_repeticoes:
        if lista[index] % numero == 0:
            agora = lista[index]
            nova_lista = agora
        agora = lista[index + 1]    
		index = index + 1
	return nova_lista