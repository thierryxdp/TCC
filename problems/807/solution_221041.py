def conta_frases(texto):
    '''retorna o numero de frases de um texto informado
    str -> int'''
    ponto_final = str.count(texto,'.')
    reticencias = str.count(texto,'...')
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    frases = ponto_final + reticencias + exclamacao + interrogacao
    
    if reticencias >= 1:
        return frases - reticencias*3
    else:
        return frases