def quant_palavras(frase):
    """função que, dada uma frase, retorne o número de palavras da frase"""
    # string -> int
    a = str.strip(frase)
    return str.count(a,' ') + 1