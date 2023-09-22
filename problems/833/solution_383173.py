def conta_numeros(numero,matriz):
    qts_aparece = 0
    i = 0
    j = 0
	while i < len(matriz):
        if numero in matriz[i]:
            qts_aparece += qts_aparece
            i += i
        while j < len(matriz[j]):
            if numero in matriz[i][j]:
                qts_aparece += qts_aparece
            	j += j
	 return qts_aparece