def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    if texto.count("...") == True:
        return texto.count("...")
    elif texto.count(".") == True:
        return texto.count(".")
    elif texto.count("...") and (".") == True:
        return (texto.count("...") + texto.count(".")) -2
    elif texto.count("?") and texto.count("!") and texto.count("...") and texto.count("."):
        return (texto.count("?") + texto.count("!")) + 2