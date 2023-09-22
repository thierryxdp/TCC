def conta_frases(frase):
    '''Retorna o numero de frases em determinada string
    str -> int'''
    
    frase2 = str.replace(frase,'...','.')
    return str.count(frase2,'.') + str.count(frase2,'?') + str.count(frase2,'!')