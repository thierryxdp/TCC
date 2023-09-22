def quant_frases(texto):
    """Esta função recebe e texto e retorna a quantidade de frases.
    str -> int"""
    return (texto.count(".") + texto.count("!") + texto.count("?") + texto.count("..."))