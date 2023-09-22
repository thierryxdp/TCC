def conta_frases(x):
    if '...' in x and '.' not in x:
    	return str.count(x, '...') + str.count(x,'!') + str.count(x, '?')

    elif '...' not in x and '.' in x:
        return str.count(x, '.') + str.count(x,'!') + str.count(x, '?') 
    
    elif '...' and '.' in x:
        return str.count(x,'.') + str.count(x, '...') + str.count(x,'!') + str.count(x, '?') 
    
    elif '...' and '.' not in x:
    	return str.count(x,'!') + str.count(x, '?')