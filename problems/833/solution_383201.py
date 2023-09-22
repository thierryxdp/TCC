def conta_numero(numero,matriz):
    n = numero
    qts_aparece = 0
    i = 0
	while i < len(matriz):
        for n in len(matriz[i]):
            if n in matriz[i]:
            qts_aparece = qts_aparece + 1
            i = i + 1
        else: 
            i = i + 1
	return qts_aparece