def quant_palavras(frase):
    """Funçao que retorna o numero de palavras de uma frase dada"""
    frase = str.strip(frase)
    palavras = str.count (frase, " ") + 1
    return palavras