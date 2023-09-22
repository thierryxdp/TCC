def conta_frases (texto):
    '''Dado um texto, retorna o numero de frases do texto.
       : str -> int
    '''
    pf = texto.split('.')
    pe = pf.split('!')
    pi = pe.split('?')
    pc = pi.split('...')
    n_frases = len (pi.split('...'))
   
    return n_frases