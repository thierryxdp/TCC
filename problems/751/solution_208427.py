def quant_palavras(frase):
    """dada uma frase, retorna o numero de palavras
    da mesma (separados por espaco)
    str -> int"""
    x = str.split(frase," ")
    return len(x)