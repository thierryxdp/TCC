def busca(frase, matriz):
    lista = []
    if frase in matriz[0]:
        for contador in range(len(matriz)):
            for contagem in range(len(matriz[contador])):
                if frase in matriz[contador][contagem]:
                    lista.append(matriz[contador])
		nova_lista = lista[0]
        nova_lista.remove(frase)
		return [nova_lista]
    else:
        return []