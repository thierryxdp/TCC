def quant_palavras(frase):
    """retorna a quantidade de palavras que uma frase
    dada como parametro tem.
    str -> int"""
    frase_separada = frase.split()
    return len(frase_separada)