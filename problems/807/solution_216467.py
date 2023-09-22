def conta_frases(texto):
    """..."""
    ponto = str.count(texto,'.')
    reticencias = str.count(texto,'...')
    interrogacao = str.count(texto,'?')
    exclamacao = str.count(texto,'!')
    return ponto - 3 + reticencias + reticencias + interrogacao + exclamacao