def conta_frases(frases):
    '''função que conta a quantidade de frases dentro de uma determinada string; str => str'''
    ponto = frases.count(".")
    exclamacao = frases.count("!")
    interrogacao = frases.count("?")
    reticencias = frases.count("...")
    pontos = ponto + exclamacao + interrogacao + reticencias
    if reticencias >= 1:
        return pontos - (reticencias*3)
    else:
        return pontos