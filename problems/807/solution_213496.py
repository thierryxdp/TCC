def conta_frases(texto):
    texto = texto.replace('...', '.')
    texto = texto.replace('..', '.')
    return texto.count('.') + texto.count('!') + texto.count('?')