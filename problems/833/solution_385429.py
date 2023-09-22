def conta_numero(numero,matriz):
    ''''''
    i = 0
	lin = len(mat)
	l1 = []
	while i < lin: 
    	if 2 in mat[0]:
        	l1 = l1 + [i]
    	i = i + 1
	return sum(l1)