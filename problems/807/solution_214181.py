def conta_frases(texto):
    """Função que dado um texto armazenado em uma string, conta o numero de 
    frases que aparecem neste texto.
    Dados de entrada: str
    Dados de saida: int"""
    if str.count(texto, "...") == 0:
        return str.count(texto, ".") + str.count(texto, "!") + str.count(texto, "?")
    return str.count(texto, ".") + str.count(texto, "!") + str.count(texto, "?") - (2 *str.count(texto, "..."))