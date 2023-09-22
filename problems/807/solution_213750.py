def conta_frases(frase):
    for char in ".!?":
        frase = frase.replace(char, "-")
    return len(str.split(frase, "-"))