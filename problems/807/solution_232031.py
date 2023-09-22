def conta_frases(texto):
    temp = 0
    temp += texto.count('!')
    temp += texto.count('?')
    temp += texto.count('.')
    temp -= 2*texto.count('...')
    return temp