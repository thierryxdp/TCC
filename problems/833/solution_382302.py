def conta_numero(numero,matriz):
    lista = []
    coluna = len(matriz[0])
    linha = len(matriz)
    proximo = 0
	for x in matriz[1]:
    	if x==numero:
            lista.append(x)
    	proximo += 1
    return lista.count(numero)