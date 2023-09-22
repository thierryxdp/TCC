def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    quantidadef = texto.count("?") + texto.count("!")
    if texto.count("...", "."):
        return quantidadef+2
    elif texto.count("?") + texto.count("!") +texto.count("...") + texto.count("."):
        quantidadef = texto.count("?") + texto.count("!") + +texto.count("...") + texto.count(".")
        return quantidadef