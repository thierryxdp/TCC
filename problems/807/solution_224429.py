def conta_frases(frase):
    ponto=frase.count(".")
    exclamacao=frase.count("!")
    interrogacao=frase.count("?")
    reticencias=frase.count("...")
    pontos=ponto+exclamacao+reticencias+interrogacao
    if reticencias >= 1:
    return pontos - reticencias*3
    return pontos