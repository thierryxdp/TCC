def conta_frases(frase):
    '''conta o numero de frases que o texto possui'''
    '''str -> str'''
    ponto = frase.count (".")
    exclamacao = frase.count("!")
    interrogacao = frase.count("?")
    reticencias = frase.count ("...")
    pontos = ponto+exclamacao+reticencias+interrogacao
    if reticencias >= 1:
        return pontos - reticencias*3
    return pontos