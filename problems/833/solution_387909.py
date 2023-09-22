def conta_numero(n, mtx):
    if (len(mtx) == 0):
        contador = 0
    
    if (len(mtx) > 0):
        n_lin     = len(mtx)
    	n_col     = len(mtx[0])
    
    	for i in range(n_lin):
        	for j in range(n_col):
            	if (mtx[i][j] == n):
                	contador = contador + 1
    
    return contador