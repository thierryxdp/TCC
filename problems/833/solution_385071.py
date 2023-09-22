def conta_numero(numero,matriz):
    cont_numero = 0
    for linha in matriz:
        for elemento in linha:
            if numero == elemento:
                cont_numero += 1
	return cont_numero