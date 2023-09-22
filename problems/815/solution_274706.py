def insere(lista_numero,n):
	lista_nova = list.insert(lista_numero, n)
    lista_nova_corrigida = list.sort(lista_nova)
    return lista_nova_corrigida