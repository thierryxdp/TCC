def faltante(x):
    n=0
    
    while n<len(x): 
    	if x[n]==n+1:
    		n=n+1
    	elif x[n]!=n+1:
        	return n+1
        else: 
            return len(x)+1