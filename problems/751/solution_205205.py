def quant_palavras(frase):
    """Retorna o número de palavras de uma frase; string -> int."""
    return len(str.split(str.rstrip(str.lstrip(frase))))