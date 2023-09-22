def posLetra(entrada):
    for i in range(len(entrada)):
    	if entrada[i] == letra:
        	acc += 1
    	if acc == 3:
        	saida = i + 1
        	break

	return saida