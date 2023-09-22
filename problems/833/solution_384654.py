def conta_numero(numero,matriz):
	contador = sum(matriz.count(numero) for i in matriz)
	return (contador)