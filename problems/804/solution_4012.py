def filtra_pares(x):
	tupla = []

  	for num in x:
    	if (num%2 == 0):
      		tupla.append(num)

  	return (tuple(tupla))