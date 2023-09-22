def conta_frases(texto):
    """Esta função recebe texto e mostra quantas frases tem
    str -> int"""
    conta_frases = texto.count(".") + texto.count("!") + texto.count("?") -2*texto.count("...")
    return conta_frases