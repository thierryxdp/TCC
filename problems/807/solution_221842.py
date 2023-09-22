def conta_frases(texto):
    '''
    retorna a quantidade de frases de um texto
    str -> int
    '''
    return (texto[0:].count('.') + texto[0:].count('!') + (texto[0:].count('...')-2) + texto[0:].count('?'))