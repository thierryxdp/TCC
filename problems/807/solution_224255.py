def conta_frases(texto):
    frases = len(texto.split('.')) + len(texto.split('!')) + len(texto.split('?')) - len(texto.split('...'))
    return frases