def conta_frases(texto):
    ponto_final = str.count(texto,'.')
    reticencias = str.count(texto,'...')
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    return ponto_final + reticencias + exclamacao + interrogacao