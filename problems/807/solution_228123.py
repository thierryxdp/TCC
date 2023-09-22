def conta_frases(texto):
    '''
    	Funcao que recebe um texto e conta o numero de frases
        que aparecem neste texto
        string -> int
    '''
    x = list.count(texto, '.')
    y = list.count(texto, '!')
    z = list.count(texto, '?')
    p = list.count(texto, '...')
    
    return len(x+y+z+p)