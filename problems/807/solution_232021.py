def conta_frases(texto):
    """funcao que conta quantas frases tem o texto;
    str->int"""
    interog=str.count(texto,'?')
    exclam=str.count(texto,'!')
    ponto=str.count(texto,'.')
    reticent=str.count(texto,'...')
    return ponto - reticent*2 + interog + exclam