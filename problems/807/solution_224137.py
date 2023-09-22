def conta_frases(texto):
    num = 0
    num += texto.count('.')
    num += texto.count('?')
    num += texto.count('!')
    num += texto.count('...')
    return num