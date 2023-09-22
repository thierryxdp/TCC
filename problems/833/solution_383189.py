def conta_numero(numero,matriz):
    qts_aparece = 0
    i = 0
    j = 0
	while i < len(matriz):
        if numero in matriz[i]:
            qts_aparece = qts_aparece + 1
            i = i + 1
        else: 
            i = i + 1
	        while j < len(matriz[j]):
            if numero in matriz[j]:
                qts_aparece = qts_aparece + 1
                j = j + 1
            else: 
            	j = j + 1
	return qts_aparece