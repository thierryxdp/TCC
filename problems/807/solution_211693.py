def conta_frases(frase):
    frase = frase.split()
    return frase.count(". ") + frase.count("!") + frase.count("?") + frase.count("...")