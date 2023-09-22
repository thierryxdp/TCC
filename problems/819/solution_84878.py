def filtraMultiplos(x,y):
	    
	    z = []
	    indice = 0
	    
	    while indice < len(x):
	        if x[indice] % y == 0:
	          z.append(x[indice])
	        indice += 1
	        
	    return z