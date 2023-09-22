def conta_frases(texto):
    '''
    	Funcao que recebe um texto e conta o numero de frases
        que aparecem neste texto
        string -> int
    '''
    x = texto.replace('.', ' ')
    y = texto.split('!', ' ')
    z = texto.split('?', ' ')
    p = texto.split('...', ' ')
    
    texto = str.split(texto)
    
    return len(texto)