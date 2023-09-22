def conta_frases(texto):
    '''Função que retorna o número de frases das informações "texto" de entrada: str -> int '''
    ponto = str.count(texto, '.')
    reticencias = str.count(texto, '...')
    interrogacao = str.count(texto, '?')
    exclamacao = str.count(texto, '!')

    return ponto -3 * reticencias + reticencias + interrogacao + exclamacao