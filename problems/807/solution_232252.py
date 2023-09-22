def conta_frases (frase):
    '''Conta a quantidade de frases, str->int'''
    x = str.count ('...',frase[0:])
    frase = list(frase)
    return frase.count ('.') + frase.count('!') + frase.count('?') - 2 * x