def conta_frases(x):
    if '...' and '.' not in x:
    	return str.count(x, '...') + str.count(x,'!') + str.count(x, '?') 

    if '...' not in x:
        return str.count(x, '.') + str.count(x,'!') + str.count(x, '?') 
  
	if '...' and '.' in x:
        return str.count(x, '...') + str.count(x,'!') + str.count(x, '?') + str.count(x,'.')