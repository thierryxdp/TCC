def conta_frases (texto):
    '''Dado um texto, retorna o numero de frases do texto.
       : str -> int
    '''
    n_frases = texto.split ('.') + texto.split('!') + texto.split('?') + texto.split('...')
    return n_frases