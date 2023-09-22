def conta_frases(texto):
    '''
    	Funcao recebe um texto e retorna 
        o numero de frases que aparecem nele
        str -> int
        
    '''
    frases = []
    
    if '. ' in texto:
        texto.split('.') = frases
	if '!' in texto:
        texto.split('!') = frases
	if '?' in texto:
        texto.split('?') = frases
	if '...' in texto:
        texto.split('...') = frases
	return len(frases)