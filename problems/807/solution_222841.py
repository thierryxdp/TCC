def conta_frases (texto):
    '''Dado um texto, retorna o numero de frases do texto.
       : str -> int
    '''
    n_frases = []
    if texto.split('.'):
        n_frases = texto.split('.')
    if texto.split('?'):
        n_frases = texto.split('?')