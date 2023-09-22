def busca(frase, matriz):
    lista = []
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if frase in matriz[contador][contagem]:
                lista.append(matriz[contador])
	if len(lista) == 0:
        return []
	if len(lista) == 1:
        lista[0].remove(frase)
        return lista
	if len(lista) == 2:
        lista[0].remove(frase)
        lista[1].remove(frase)
        return lista