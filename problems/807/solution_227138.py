def conta_frases(texto):
    '''Dado um texto, retorna o numero de frases nesse texto;
    string -> int'''
	return str.count(texto, '.' + ' ') + 
			str.count(texto, '!') + 
    		str.count(texto, '?') + 
        	str.count(texto, '...')