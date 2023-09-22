def conta_frases(texto):
    """conta o numero de frases de um texto"""
    x=texto.split('.')
    x=texto.split('?')
    x=texto.split('!')
    x=texto.split('...')
    y=len(texto)
    return y