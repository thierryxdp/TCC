def conta_numeros(numero,matriz):
    qts_apareceL = 0
    qts_apareceC = 0
    i = 0
    j = 0
	while i < len(matriz):
        if numero in matriz[i]:
            qts_apareceL += qts_apareceL
            i += i
        while j < len(matriz[j]):
            if numero in matriz[j]:
                qts_apareceC += qts_apareceC
            	j += j
	return qts_apareceL + qts_apareceC