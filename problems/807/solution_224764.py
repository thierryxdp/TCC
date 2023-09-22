def conta_frases(texto):
    """Conta a quantidade de frases que aparecem no texto
    str->int"""
    exclamacoes=str.count(texto,'!')
    interrogacoes=str.count(texto,'?')
    reticencias=str.count(texto,'...')
    ponto=str.count(texto,'.')
    n_de_frases=exclamacoes+interrogacoes+reticencias+ponto
    return n_de_frases