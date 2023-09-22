def conta_frases(texto):
    ponto_final = str.count(texto,'.')
    reticencias = str.count(texto,'...')
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    frases = ponto_final + reticencias + exclamacao + interrogacao
    
    if reticencias >= 1:
        return frases - reticencias*3
    else:
        return frases