def conta_numero(numero,matriz):
    cont = 0
    if len(matriz) > 1:
        for i in matriz:
            for j in i:
                if j == numero:
                    cont+= 1
		return cont
    else:
        for i in matriz:
            if i == numero:
                cont+= 1
		return cont