def conta_frases(texto):
    '''
    	Funcao que recebe um texto e conta o numero de frases
        que aparecem neste texto
        string -> int
    '''
    p = texto.count('...')
    x = texto.count('.')
    y = texto.count('!')
    z = texto.count('?')
    
    return x+y+z+p