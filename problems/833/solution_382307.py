def conta_numero(numero,matriz):
    lista = []
    coluna = len(matriz[0])
    linha = len(matriz)
    proximo = 0
	for x in range(linha):
        for y in range(coluna):
    		if y==numero:
            	lista.append(x)
    return lista.count(numero)