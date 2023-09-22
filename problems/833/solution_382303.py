def conta_numero(numero,matriz):
    lista = []
    coluna = len(matriz[0])
    linha = len(matriz)
    proximo = 0
	for x in linha:
        for y in coluna:
    		if matriz[x][y]==numero:
            	lista.append(x)
    return lista.count(numero)