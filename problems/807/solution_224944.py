def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    reticencias = (texto.count("...")-2)
    elif texto.count("..."):
        return reticencias
    if texto.count("?") and texto.count("!") and texto.count("...") and texto.count("."):
        return (texto.count("?") + texto.count("!")) + 2
    elif texto.count("?"):
        return texto.count("?")
    elif texto.count("."):
        return texto.count(".")
    elif texto.count("...") and ("."):
        return (texto.count("...") + texto.count(".")) -2