def conta_frases (texto:str) -> int:
    """Função que irá contar o número de frases de um texto.
    """

    return str.count(texto, ".") + str.count(texto, "!") + str.count(texto, "?") + str.count(texto, "...")