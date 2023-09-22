def conta_frases(texto):
    exclamacao = texto.count('!')
    interrogacao = texto.count('?')
    reticencias = texto.count('...')
    ponto = texto.count('.')

    numero_frases = exclamacao + interrogacao + reticencias + ponto
    if reticencias > 0:
        numero_frases -= 3 * reticencias
    return numero_frases