def busca(frase, matriz):
    lista = []
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if frase in matriz[contador][contagem]:
                list.exteded(lista, matriz[contador][0])
				list.extended(lista, matriz[contador][1])
				list.extended(lista, matriz[contador][3])
	return lista