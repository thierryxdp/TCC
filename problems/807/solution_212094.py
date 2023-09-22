def conta_frases(texto):
    '''Retorna o número de frases que aparecem no texto dado'''
    '''str --> int'''
    pontos = str.count(texto,'.')
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    reticencias = str.count(texto,'...')-3*str.count(texto,'...')
    return pontos+exclamacao+interrogacao+reticencias