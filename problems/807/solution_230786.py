def conta_frases(texto):
    '''funcao que conta o numero de frases que tem o texto
    str->int'''
    interog=str.count(texto,'?')
    exclam=str.count(texto,'!')
    ponto=str.count(texto,'.')
    reticent=str.count(texto,'...')
    return ponto - reticent*2 + interog + exclam