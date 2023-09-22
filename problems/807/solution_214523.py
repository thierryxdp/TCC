def conta_frases(texto):
    """Conta a quantidade de palavras em um texto;
    string -> int"""
    return texto.count("!") + texto.count(".") + texto.count("?") + texto.count("...") for "." == "..."