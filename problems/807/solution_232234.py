def conta_frases (frase):
    '''Conta a quantidade de frases, str->int'''
    frase = str.split(frase)
    if 'aula...' or 'dacolá...' in frase:
        frase = list(frase)
        return frase.count ('.') + frase.count('!') + frase.count('?')
    else:
        frase = list(frase)
        return frase.count ('.') + frase.count('!') + frase.count('?')