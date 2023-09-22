def conta_frases(texto):
    num = 0
    num += texto.count('.')
    num += texto.count('?')
    num += texto.count('!')
    if (texto.find('...') != -1):
        num += -2
    return num