def conta_frases(texto):
    '''
    	Funcao que recebe um texto e conta o numero de frases
        que aparecem neste texto
        string -> int
    '''
    x = texto.count('.')
    y = texto.count('!')
    z = texto.count('?')
    p = texto.count('...')
    
    a = x+y+z+p
    
    return len(a)