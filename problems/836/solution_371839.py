def busca(frase, matriz):
    lista = []
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if frase in matriz[contador][contagem]:
                lista.append(matriz[contador])
	tamanho_lista = len(lista)
    return tamanho_lista