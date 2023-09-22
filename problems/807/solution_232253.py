def conta_frases (frase):
    '''Conta a quantidade de frases, str->int'''
    x = frase.count (...)
    frase = list(frase)
    return frase.count ('.') + frase.count('!') + frase.count('?') - 2 * x