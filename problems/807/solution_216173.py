def conta_frases(texto):
    '''Função que dado um texto, retorna o numero de frases.
    string -> int'''
    interrogacao = str.count(texto, '?')
    exclamacao = str.count(texto, '!')
    reticencias = str.replace(texto, '...', '*')
    reticencias2 = str.count(reticencias, '*')
    ponto = str.count(reticencias, '.')
    return interrogacao + exclamacao + ponto + reticencias2