def conta_frases (frase):
    '''
    str -> int
    '''
    return (str.count(frase,'.'))+(str.count(frase,'!'))+(str.count(frase,'?')+(str.count(frase,'...'))