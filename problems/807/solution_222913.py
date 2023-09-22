def conta_frases (texto):
    '''Dado um texto, retorna o numero de frases do texto.
       : str -> int
    '''
    x = texto.replace('!','.')
    x1 = x.replace('?','.')
    x2 = x1.replace('...','.')
    
    n_frases = x2.count('.')
   # n_frases = texto.count('.')
    return n_frases