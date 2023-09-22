def conta_numero(numero,matriz):
    qts_aparece = 0
    i = 0
	while i < len(matriz):
        for numero in range(len(matriz[i])):
            qts_aparece = qts_aparece + 1
            i = i + 1
        else: 
            i = i + 1
	return qts_aparece