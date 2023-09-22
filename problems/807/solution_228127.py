def conta_frases(texto):
    '''
    	Funcao que recebe um texto e conta o numero de frases
        que aparecem neste texto
        string -> int
    '''
    x = texto.replace('.', ' ')
    y = texto.replace('!', ' ')
    z = texto.replace('?', ' ')
    p = texto.replace('...', ' ')
    
    texto = str.split(texto)
    
    return len(texto)