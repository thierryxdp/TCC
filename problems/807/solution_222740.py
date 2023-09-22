def conta_frases (texto):
    '''Dado um texto, retorna o numero de frases do texto.
       : str -> int
    '''
    pf = str (texto.split('.'))
    pe = str (pf.split('!'))
    pi = str (pe.split('?'))
    pc = pi.split('...')
    n_frases = len (pi.split('...'))
   
    return n_frases