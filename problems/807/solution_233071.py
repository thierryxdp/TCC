def conta_frases(frase):
    '''Dado um trecho, conta o número de frases presentes.'''
    quantidade = str.count(frase,'.') + str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'...')
    return quantidade