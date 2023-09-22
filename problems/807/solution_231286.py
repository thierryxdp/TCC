def conta_frases(x):
    if '...' in x and '.' not in x:
    	return str.count(x, '...') + str.count(x,'!') + str.count(x, '?')

    if '...' not in x and '.' in x:
        return str.count(x, '.') + str.count(x,'!') + str.count(x, '?')