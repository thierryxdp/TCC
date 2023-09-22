def conta_frases(texto):
    '''conta o numero de frases que aparecem neste texto'''
    ponto=texto.count(".")
    exclamacao=texto.count("!")
    interrogacao=texto.count("?")
    reticencias=texto.count("...")
    pontos=ponto+exclamacao+reticencias+interrogacao
    if reticencias >= 1:
        return pontos-reticencias*3
    return pontos