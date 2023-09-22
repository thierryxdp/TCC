def conta_frases(texto):
    num = texto.count('.')
    num += texto.count('?')
    num = texto.count('!')
    num = texto.count('...')
    return num