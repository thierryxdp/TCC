def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    reticencias = texto.count("...")
    if (texto.count("...") == True) and (texto.count("?") and texto.count("!") and texto.count(".") == False):
        return texto.count("...")
    elif texto.count("?") and texto.count("!") and texto.count("...") and texto.count("."):
        return (texto.count("?") + texto.count("!")) + 2
    elif texto.count("?"):
        return texto.count("?")
    elif texto.count("."):
        return texto.count(".")
    elif texto.count("...") and ("."):
        pontos = (texto.count("...") + texto.count(".")) -2
        return pontos