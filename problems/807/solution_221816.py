def conta_frases(texto):
    '''
    retorna a quantidade de frases de um texto
    str -> int
    '''
    reticencias='...'
    return (texto[0:].count('.') + texto[0:].count('!') + texto[0:].count('reticencias') + texto[0:].count('?'))