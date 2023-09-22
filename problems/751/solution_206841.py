def quant_palavras(frase):
    """Calcula a quantidade de palavras numa frase; str -> int"""
    x = str.split(frase)
    return int(len(x))