def conta_frases(frases):
    '''Retorna a quantidade de frases a cada ponto.
    STR->INt'''
    frases= frases.replace('!','.')
    frases= frases.replace('?','.')
    frases= frases.replace('...','.')
    return str.count(frases,'.')