def filtraMultiplos(x,y):
2	    
3	    z = []
4	    indice = 0
5	    
6	    while indice < len(x):
7	        if x[indice] % y == 0:
8	          z.append(x[indice])
9	        indice += 1
10	        
11	    return z