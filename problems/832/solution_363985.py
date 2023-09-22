def eh_quadrada(mtx):
    
    if (mtx == []):
        return True
    
    else:
        n_lin = len(mtx)
        n_col = len(mtx[0])
    
    	if (n_lin == n_col):
        	return True
    	
    	if (n_lin != n_col):
        	return False