def conta_frases(frase):
    ponto=frase.count(".")
    exclamacao=frase.count("!")
    interrogacao=frase.count("?")
    reticencias=()
    if ponto == 3:
        reticencias=ponto
    pontos=ponto+exclamacao+reticencias+interrogacao
    return pontos