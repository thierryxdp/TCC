def conta_frases(texto):
    '''
    função que retorna o número de frases de um texto;
    str -> int
    '''
    ponto_final = str.count(texto, '.')
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    reticencias = str.count(texto, '...')
    return ponto_final + exclamacao + interrogacao + (reticencias -3)