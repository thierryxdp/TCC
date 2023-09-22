def filtra_pares(tupl):
    par=()
	if tupl[0]%2==0:
    	par+=(tupl[0],)
    	if tupl[1]%2==0:
    	    par+=(tupl[1],)
    	    if tupl[2]%2==0:
    	        par+=(tupl[2],)
                if tupl[3]%2==0:
    	            par+=(tupl[3],)
    	            return par
    	        return par
    	    return par
    	return par
	elif tupl[1]%2==0:
    	par+=(tupl[1],)
	    if tupl[2]%2==0:
	        par+=(tupl[2],)
	      	if tupl[3]%2==0:
	            par+=(tupl[3],)
	            return par
	        return par
	    return par
    elif tupl[2]%2==0:
        par+=(tupl[2],)
       	if tupl[3]%2==0:
	        par+=(tupl[3],)
	        return par
        return par
	elif tupl[3]%2==0:
        par+=(tupl[3],)
        return par
    else:
        return par