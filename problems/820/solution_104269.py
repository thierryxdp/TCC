def posLetra(entrada, letra, n):
    acc = 0
    for i in range(len(entrada)):
    	if entrada[i] == letra:
        	acc += 1
    	if acc == n:
        	saida = i + 1
        	break

	return saida