def conta_frases(frase):
    """Dado um texto, conta o número de frases, considerando cada pontuação encerrando uma frase
    str -> int"""
    x = frase
    if "." in x:
        return str.count(x, ".") + str.count(x, "!") + str.count(x, "?") + str.count(x, "...") - str.count(x, "...") - str.count(x, "...") - str.count(x, "...")
    if "." not in x:
        return str.count(x, "!") + str.count(x, "?") + str.count(x, "...")