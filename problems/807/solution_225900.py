def conta_frase(texto):
    """conta o numero de frases de um texto"""
    x=texto.split('.')
    x=texto.split('?')
    x=texto.split('!')
    x=texto.split('...')
    x=len(texto)
    return x