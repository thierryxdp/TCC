def conta_numero(numero,matriz):
    lista = []
    coluna = len(matriz[0])
    linha = len(matriz)
    proximo = 0
	for x in matriz:
    	lista.append(x[proximo])
        proximo += 1
    return lista