def conta_frases(x):
    if '...' in x:
    	return str.count(x, '...') + str.count(x,'!') + str.count(x, '?') 

    if '...' not in x:
        return str.count(x, '.') + str.count(x,'!') + str.count(x, '?') 
    
    if '.' in x:
        return str.count(x,'.')  + str.count(x,'!') + str.count(x, '?')