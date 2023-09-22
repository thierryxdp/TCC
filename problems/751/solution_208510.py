def quant_palavras(frase):
    """Recebe uma frase e retorna o número de palavras
dela.
str -> int
"""
    palavras = str.split(frase)
    return len(palavras)