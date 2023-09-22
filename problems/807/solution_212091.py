def conta_frases(texto):
    '''Retorna o número de frases que aparecem no texto dado'''
    '''str --> int'''
    pontos=str.count(texto,'.')
    exclamação=str.count(texto,'!')
    interrogação=str.count(texto,'?')
    reticencias=str.count(texto,'...')
    return pontos+exclamação+interrogação+reticencias