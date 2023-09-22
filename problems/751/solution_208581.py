def quant_palavras(frase):
    """Recebe uma frase e retorna o número de palavras
dela através da contagem dos pedaços gerados pelo comando
split.
str -> int
"""
    palavras = str.split(frase)
    return len(palavras)