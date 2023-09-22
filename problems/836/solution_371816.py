def busca(frase, matriz):
    lista = []
    for contador in matriz:
        for contagem in contador:
            if frase in matriz[contador][contagem]:
                list.append(lista, matriz[contador][contagem])
	return lista