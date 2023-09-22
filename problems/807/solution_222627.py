def conta_frases(texto):
    """Funcao que conta o numero de frases contidas no texto dado
    entrada: string
    saida: int""" 
    return str.count(texto, "?") + str.count(texto, "!") + str.count(texto, "...") + str.count(texto, ". ") + str.count(texto, ".",-1)