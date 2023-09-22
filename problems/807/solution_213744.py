def conta_frases(frase):
    for char in ".!?":
        frase = frase.replacer(char, "")
    return frase