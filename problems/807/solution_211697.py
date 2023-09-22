def conta_frases(frase):
    frase = frase[0]
    return frase.count(". ") + frase.count("!") + frase.count("?") + frase.count("...")