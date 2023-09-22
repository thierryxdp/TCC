def conta_frases(texto):

    reticencias = texto.count('...')
    exclamacao = texto.count('!')
    interrogacao = texto.count('?')
    pontos = texto.count('.')
    
    if reticencias > 0:
        return reticencias + exclamacao + interrogacao + pontos - 3*reticencias
    else:
        return exclamacao + interrogacao + pontos