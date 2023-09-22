def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    texto.replace('...','.')
    if (texto.count("...") and (".")) == True and (texto.count("?") and texto.count("!") and texto.count(".")) == False:
        return (texto.count("...") -4) + texto.count(".")