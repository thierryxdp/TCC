def conta_frases(texto):
    """Função que retona uma frase ate seu caractere"""
    return str.count(texto, ".") + str.count(texto, "!") + str.count(texto, "?") + str.count(texto, "...")