def conta_frases1(texto):
    """funcao que calcula o numero de frases que aparecem em determinado texto, a partir
    da sua pontuacao, onde ".", "...", "?", "!" sao separadores de frases;
    str -> int"""
    cometc = str.count(texto, ".") - (str.count(texto, "...") * 2)
    frases = str.count(texto, ".") + str.count(texto, "!") + str.count(texto, "?")
    if "..." in texto:
        return cometc + str.count(texto, "!") + str.count(texto, "?")
    return frases