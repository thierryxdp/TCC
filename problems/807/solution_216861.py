def conta_frases(texto):
    num = texto.count('.') + texto.count('!') + texto.count('?') + texto.count('...')
    return num