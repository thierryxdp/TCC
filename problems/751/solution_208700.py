def quant_palavras(frase):
    """Ao receber uma frase, retorna o número de palavras
    str -> int"""
    l_palavras = str.split(frase,' ')
    quantidade = len(l_palavras)
    return quantidade