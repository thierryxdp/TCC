def conta_frases (texto):
    '''Dado um texto, retorna o numero de frases do texto.
       : str -> int
    '''
    x = texto.replace('!','.')
    x = texto.replace('?','.')
    x = texto.replace('...','.')
    
    n_frases = texto.count()