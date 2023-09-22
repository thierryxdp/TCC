def quant_palavras(frase):
    """Dada uma frase, retorna o número de palavras dela
    str -> int"""
    num_palavras = str.count(frase, ' ') + 1
    return num_palavras