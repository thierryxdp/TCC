def conta_frases(texto):
    exc = str.count(texto,'!')
    inter = str.count(texto,'?')
    ret = str.count(texto,'...')
    pontos = str.count(texto,'.')
    pontos_finais = pontos - ret*3
    return exc + inter + ret + pontos_finais