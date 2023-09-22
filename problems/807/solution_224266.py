def conta_frases(texto):
    texto = texto.replace('!', '.')
    texto = texto.replace('?', '.')
    texto = texto.replace('...', '.')
    frases = len(texto.split('.'))
    return frases