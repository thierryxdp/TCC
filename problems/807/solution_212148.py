def conta_frases(texto):
    """Essa funcao conta o numero de frases em um dado texto
    string -> int
    """
    ponto_final = str.count(texto,'.')
    ponto_exclamacao = str.count(texto,'!')
    ponto_interrogacao = str.count(texto,'?')
    reticencias = str.count(texto,'...')
    return ponto_final + ponto_exclamacao + ponto_interrogacao + reticencias - 3*reticencias