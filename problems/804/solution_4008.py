def filtra_pares(x):
	tupla = []

  	for i in range(len(x)):
    	w = x[i]//2
        if (w == 0):
      		tupla.append(x[i])

  	return (tuple(tupla))