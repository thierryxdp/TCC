def quant_palavras(frase):
    """recebe uma frase e retorna o numero de palavras nela
    contida,
    str -> int"""
    palavras = str.split(frase)
    return len(palavras)