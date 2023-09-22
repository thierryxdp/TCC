def conta_frases(frase):
    '''conta o número de frases dentro da sentença'''
    ponto = '!' or '.' or '?' or '...'
    return str.count(frase,ponto)