def conta_frases(frase):
    for char in ".!?":
        frase = frase.split(char, "")
    return frase