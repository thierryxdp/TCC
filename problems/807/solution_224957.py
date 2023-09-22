def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    reticencias = texto.count("...")
    if (texto.count("...") == True) and (texto.count("?") and texto.count("!") and texto.count(".") == False):
        return texto.count("...")