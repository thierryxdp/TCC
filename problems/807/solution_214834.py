def conta_frases(texto):

    reticencias = Texto.count('...')
    exclamacao = Texto.count('!')
    interrogacao = Texto.count('?')
    pontos = Texto.count('.')
    
    if reticencias > 0:
        return reticencias + exclamacao + interrogacao + pontos - reticencias
    else:
        return exclamacao + interrogacao + pontos