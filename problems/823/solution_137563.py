def faltante(x):
    i=0  
    list.sort(x)
    while (i+1)<=max(x):
    	if x[i] != (i+1):
        	return i+1
        elif (i+1)==max(x):
            return i+2
        else:
    		i=i+1