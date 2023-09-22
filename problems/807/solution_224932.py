def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    if texto.count{"...") == True:
        return 1
    elif texto.count("...") and (".") == True:
        return 2
    elif texto.count("?") and texto.count("!") and texto.count("...") and texto.count("."):
        return texto.count("?") + texto.count("!") + 2