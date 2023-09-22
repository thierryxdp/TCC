frequencia = {}
		texto = texto.split()
    	for i in range(len(texto)):
        	if texto[i] in frequencia:
            	frequencia[texto[i]] += 1
        	if texto[i] not in frequencia:
            	frequencia[texto[i]] = 1
    	return frequencia