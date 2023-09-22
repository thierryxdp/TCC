def conta_frases (texto):
    reticencias = str.count (texto, '...')
    ponto = str.count(texto,'.')-3*reticencias
    interrogacao = str.count (texto, '?')
    exclamacao = str.count (texto, '!')
    return ponto + interrogacao + reticencias + exclamacao