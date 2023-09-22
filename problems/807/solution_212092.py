def conta_frases(texto):
    '''Retorna o número de frases que aparecem no texto dado'''
    '''str --> int'''
    pontos=str.count(texto,'.')
    exclamacão=str.count(texto,'!')
    interrogacão=str.count(texto,'?')
    reticencias=str.count(texto,'...')
    return pontos+exclamacão+interrogacão+reticencias