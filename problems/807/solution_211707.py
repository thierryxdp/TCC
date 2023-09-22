def conta_frases(frase):
    if "..." in frase:
        pontos = frase.count(".") - 2*frase.count("...")
    else:
        pontos = frase.count(".")
    return frase.count("!") + frase.count("?") + pontos