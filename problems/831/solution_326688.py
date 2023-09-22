def lingua_p(palavra):
    """ Altera a palavra de entrada, traduzindo ela para a lingua do p"""
    """str -> str"""
    palavra.lower
    vogais= "aàáãâeéêiíoóôúu"
    alterada = ""
    for letra in palavra:
        if letra in vogais:
            alterada += letra + "p" + letra
        else:
            alterada += letra
    return alterada