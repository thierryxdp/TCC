def conta_frases (frase):
    '''Conta a quantidade de frases, str->int'''
    frase = str.split(frase)
    'aula...' = '.'
    'tarde...' = '.'
    'dacolá...' = '.'
    'estimação...' = '.'
    frase = list(frase)
    return frase.count ('.') + frase.count('!') + frase.count('?')