def conta_frases(texto):
    '''
    	Funcao que recebe um texto e conta o numero de frases
        que aparecem neste texto
        string -> int
    '''
    if '...' in texto:
        x = texto.count('...')
    if '.' in texto:
        y = texto.count('.')
    if '!' in texto:
        z = texto.count('!')
    if '?' in texto:
    	p= texto.count('?')
    
    return x+y+z+p