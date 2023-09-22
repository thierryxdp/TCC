def busca(frase, matriz):
    lista = []
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if frase in matriz[contador][contagem]:
                lista.append(matriz[contador])
		nova_lista = lista[contador]
		nova_lista.remove(frase)
	return nova_lista