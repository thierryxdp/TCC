def conta_frases (frase):
    '''Conta a quantidade de frases, str->int'''
    frase = str.split(frase)
    if 'aula...' or 'tarde...' or 'dacolá...' or 'estimação...' not in frase:
        frase = list(frase)
        return frase.count ('.') + frase.count('!') + frase.count('?')
    elif 'aula...' or 'dacolá...' in frase:
        return frase.count ('.') + frase.count('!') + frase.count('?') - 2
    else:
        return frase.count ('.') + frase.count('!') + frase.count('?') - 4