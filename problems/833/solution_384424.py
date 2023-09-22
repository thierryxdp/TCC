def conta_numero(numero,matriz):
    m = matriz [:]
    conta = 0
	for lista in matriz:
		for elem in lista:
            if elem == numero:
				conta+=1
	return conta