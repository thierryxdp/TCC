def conta_frases(texto):
    '''Funcao que conta o numero de frases dentro de um texto'''
    '''str -> int'''
    frase1 = str.split(texto,'?')
    frase2 = str.split(texto,'!')
    frase3 = str.split(texto,'.')
    frase4 = str.split(texto,'...')
    return len(frase1+frase2+frase3+frase4)