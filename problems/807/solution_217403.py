def conta_frases(texto):
    ''' conta o número de frases no texto
    string -> int'''
    if '.' and '...' in texto:
    	return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?') - (str.count(texto,'...')*2)
	
    elif '.' in texto:
    	return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?')