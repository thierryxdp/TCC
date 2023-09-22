def conta_frases(frase):
    """Dado um texto, conta o número de frases do texto, considerando cada pontuação como um final de frase"""
    x = frase
    if "." in x:
        return str.count(x, ".") + str.count(x, "!") + str.count(x, "?") + str.count(x, "...") - str.count(x, "...") - str.count(x, "...") - str.count(x, "...")
    if "." not in x:
        return str.count(x, "!") + str.count(x, "?") + str.count(x, "...")