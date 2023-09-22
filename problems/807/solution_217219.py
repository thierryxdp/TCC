def conta_frases(texto):
    """ essa funcao calcula o numero de frases que a nela;int ->int """
    ponto=str.count(texto,'.')
    reticencias=str.count(texto,'...')
    interrogacao=str.count(texto,'?')
    exclamacao=str.count(texto,'!')
    
    return ponto -3*reticencias+reticencias+interrogacao+exclamacao