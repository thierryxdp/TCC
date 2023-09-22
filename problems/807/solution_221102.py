def conta_frases(texto):
    '''Dado um texto, retorna o numero de frases
    que aparecem nesse texto
    str -> int'''
    exc = str.count(texto,'!')
    inter = str.count(texto,'?')
    ret = str.count(texto,'...')
    pontos = str.count(texto,'.')
    pontos_finais = pontos - ret*3
    return exc + inter + ret + pontos_finais