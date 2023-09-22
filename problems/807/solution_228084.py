def conta_frases(frase):
    '''função que conta o numero de frases
    string -> int'''
    x = frase
    y = '...'
    z = '. '
    return x.count('!') + x.count('?') + x.count(z) + x.count(y) + x.count('.')