def conta_frases(frase):
    ponto=frase.count(".")
    exclamacao=frase.count("!")
    interrogacao=frase.count("?")
    reticencias=frase.count("...")
    pontos=ponto+exclamacao+reticencias+interrogacao
    return pontos