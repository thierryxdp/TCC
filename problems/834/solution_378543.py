def media_matriz(matriz):
    soma = 0
    qtd = 0
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            soma = soma + matriz[contador][contagem]
            qtd = qtd + 1
	return soma/qtd