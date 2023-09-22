def quant_palavras(frase):
    """Dada uma frase, esta função retorna o número de palavras
    da frase.
    str -> int """
    
    palavras = str.split(frase)
    
    return len(palavras)