def conta_frases(texto):
    '''Funcao que conta o numero de frases dentro de um texto'''
    '''str -> int'''
    frase = str.split(texto,' ')
    return str.count(frase)