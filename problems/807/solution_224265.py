def conta_frases(texto):
    texto.replace('!', '.')
    texto.replace('?', '.')
    texto.replace('...', '.')
    frases = len(texto.split('.'))
    return frases