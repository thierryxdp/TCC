def conta_frases(frase):
    """ calcula e retorna o numero de frases de acordo com a pontuação final delas"""
    x = frase
    if "." in x:
        return str.count(x, ".") + str.count(x, "!") + str.count(x, "?") + str.count(x, "...") - str.count(x, "...") - str.count(x, "...") - str.count(x, "...")
    if "." not in x:
        return str.count(x, "!") + str.count(x, "?") + str.count(x, "...")