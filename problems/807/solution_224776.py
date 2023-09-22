def conta_frases(texto):
    '''Retorna o número de frases que um texto possui
    str->int'''
    pontos=str.count(texto,'.')
    tres_pontos=str.count(texto,'...')
    ponto_exc=str.count(texto,'!')
    ponto_int=str.count(texto,'?')
    pontos=pontos-(3*tres_pontos)
    return pontos+tres_pontos+ponto_exc+ponto_int