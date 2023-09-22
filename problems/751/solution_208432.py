def quant_palavras(frase):
    """
    retorna o número de palavras em uma frase
    str -> int
    """
    separados = str.split(frase)
    return len(separados)