def conta_frases(texto):
    '''
    	Funcao que recebe um texto e conta o numero de frases
        que aparecem neste texto
        string -> int
    '''
    x = texto.split('.')
    y = texto.split('!')
    z = texto.split('?')
    p = texto.split('...')
    
    return len(x-y-z-p)