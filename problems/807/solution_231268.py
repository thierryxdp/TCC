def conta_frases(x):
    if '...' in x:
    	return str.count(x, '...') + str.count(x,'!') + str.count(x, '?')