def conta_frases (frase):
    '''Conta a quantidade de frases, str->int'''
    frase = str.split(frase)
    x = frase.count ("aula...") 
    frase = list(frase)
    return frase.count ('.') + frase.count('!') + frase.count('?') - 2 * x