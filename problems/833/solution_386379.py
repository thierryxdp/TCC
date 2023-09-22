def conta_numero(numero,matriz):
    cont = 0
    for i in matriz:
        for j in i:
            if j == numero:
                cont+= 1
	return cont