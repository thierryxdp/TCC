def quant_palavras(frase):
    """Retorna o número de palavras da frase dada."""
    '''str -> int'''
    return len(str.split(str.strip(frase)))