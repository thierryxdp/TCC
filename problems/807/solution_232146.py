def conta_frases (frase):
    '''Conta a quantidade de frases que há num texto, str->int'''
    return str.count ('.',frase[0:] + str.count ('?',frase[0:] + str.count ('!',frase[0:]