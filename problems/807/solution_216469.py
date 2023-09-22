def conta_frases(texto):
    """Função que conta o número de frases que aparecem no texto,
    st --> int"""
    ponto = str.count(texto,'.')
    reticencias = str.count(texto,'...')
    interrogacao = str.count(texto,'?')
    exclamacao = str.count(texto,'!')
    return ponto - 3 * reticencias + reticencias + interrogacao + exclamacao