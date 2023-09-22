def conta_frases(texto):
    result = len(texto.split('?'), texto.split('.'), texto.split('...'), texto.split('!'))
    return result