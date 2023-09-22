def conta_numero(numero,matriz):
    ''''''
    i = 0
	lin = len(matriz)
	l1 = []
	while i < lin: 
    	if numero in matriz[0]:
        	l1 = l1 + [i]
    	i = i + 1
	return sum(l1)