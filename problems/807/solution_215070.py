def quant_frases(texto):
    """Esta função recebe um texto e retorna a quantidade de frases.
    str -> int"""
    return (str(texto.count(".")) + str(texto.count("!")) + str(texto.count("?")) + str(texto.count("...")))