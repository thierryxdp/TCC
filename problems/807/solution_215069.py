def quant_frases(texto):
    """Esta função recebe e texto e retorna a quantidade de frases.
    str -> int"""
    return (str.count(texto,".") + str.count(texto,"!") + str.count(texto,"?") + str.count(texto,"..."))