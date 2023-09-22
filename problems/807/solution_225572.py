def conta_frases(texto):
    """a partir de uma string texto, retorna o numero de
    frases contidos na string texto.
    str -> int"""
    interrogacao = str.count(texto,'?')
    exclamacao = str.count(texto,'!')
    final = str.count(texto,'.')
    reticencias = str.count(texto,'...')
    return interrogacao + exclamacao + final + reticencias