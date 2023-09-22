def busca(frase, matriz):
    lista = []
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if frase in matriz[contador][contagem]:
                lista.append(matriz[contador])
	tamanho_lista = len(lista)
    nova_lista = lista[tamanho_lista].remove(frase)
    return nova_lista