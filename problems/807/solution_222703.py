def conta_frases(frase):
    ponto=frase.count(".")
    exclamacao=frase.count("!")
    interrogacao=frase.count("?")
    reticencias=frase.count("...")
    if ponto == "...":
        count=1
        reticencias=ponto
    pontos=ponto+exclamacao+reticencias+interrogacao
    return pontos