def conta_frases(x):
    ponto = str.count(x,'.')
    exc = str.count(x,'!')
    retcs = str.count(x,'...')
    interrog = str.count(x,'?')
    
    if ponto>0 and exc>0 and retcs>0 and interrog>0:
    	return x = ponto + exc + retcs + interrog
	
    elif ponto=0 and exc>0 and retcs>0 and interrog>0:
       	return x = exc + retcs + interrog
    
    elif ponto>0 and exc=0 and retcs>0 and interrog>0:
		return x = ponto + retcs + interrog
    
    elif ponto>0 and exc>0 and retcs=0 and interrog>0:
        return x = ponto + exc + interrog

    elif ponto>0 and exc>0 and retcs>0 and interrog=0:
        return x = ponto + exc + retcs