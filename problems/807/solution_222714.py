def conta_frases (texto):
    '''Dado um texto, retorna o numero de frases do texto.
       : str -> int
    '''
    a = texto.replace('!','.')
    b = texto.replace('?','.')
    c = texto.replace('...','.')
    
    n_frases = len(texto.split('.')):
        return n_frases