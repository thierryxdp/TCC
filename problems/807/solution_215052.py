def conta_frases(texto):
    """"Função que dado um texto armazenado em uma string, conta o número de frases que aparecem neste texto.
    str -> int """

    return texto.index(".") + texto.index("...") + texto.index("!") + texto.index("?")