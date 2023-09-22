def conta_frases (frase):
    '''
    str -> int
    '''
    return int(frase.count(str('.'))+frase.count(str('!'))+frase.count(str('?'))+frase.count(str('...')))