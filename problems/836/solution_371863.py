def busca(frase, matriz):
    lista = []
	soma_cont = 0
    soma_while = 0
    for contador in range(len(matriz)):
        soma_cont = soma_cont + 1
        for contagem in range(len(matriz[contador])):
            if frase in matriz[contador][contagem]:
                lista.append(matriz[contador])
	while soma_while <= soma_cont:
        lista[soma_while].remove(frase)
	return lista