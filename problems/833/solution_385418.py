def conta_numero(numero,matriz):
    vezes = 0
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if matriz[contador][contagem] == numero:
                vezes = vezes + 1
	return vezes