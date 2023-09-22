def conta_numero(numero,matriz):
    ''''''
    i = 0
	lin = len(matriz)
	l1 = []
	while i < lin: 
    	if numero in mat[i]:
        	l1 = l1 + [list.index(mat[i],0)]
    	i = i + 1
	return(len(l1))