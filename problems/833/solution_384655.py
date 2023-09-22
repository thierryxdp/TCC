def conta_numero(numero,matriz):
	contador = sum(i.count(numero) for i in matriz)
	return (contador)