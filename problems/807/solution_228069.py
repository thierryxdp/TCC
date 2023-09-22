def conta_frases(frase):
    '''função que conta o numero de frases
    string -> int'''
    x = frase
    return x.count('!', '?', '.') + x.count('...')