def conta_frases(frase):
    f = frase.split(".") and frase.split("...") and frase.split("!") and frase.split("?")
    return len(f)