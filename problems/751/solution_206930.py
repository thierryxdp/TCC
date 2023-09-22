def quant_palavras(frase):
    """retona numero de palavras da frase considerando que a frase pode ter espacos no inicio e no final.
    str->str"""
    frase = str.split(frase)
    return len(frase)