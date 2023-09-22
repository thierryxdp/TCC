def conta_frases(texto):
    """função que conta as frases de um determinado texto baseado na quantidades de pontos.
    str -> int"""
    "..." = 1
    str.count(texto,".")
    str.count(texto,"!")
    str.count(texto,"?")
    str.count(texto,"...")
    return str.count(texto,"...") + str.count(texto,"!") + str.count(texto,"?") + str.count(texto,".")