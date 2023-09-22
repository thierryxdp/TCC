iltraMultiplos(lista,n):
    x = []
    proximo = 0
	while proximo <len(lista):
		if lista[proximo]%n == 0:
			x = x + [lista[proximo]]
	proximo = proximo + 1
	return x