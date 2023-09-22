def conta_frases(frase):
    frase = frase[0].split()
    return frase.count(". ") + frase.count("!") + frase.count("?") + frase.count("...")