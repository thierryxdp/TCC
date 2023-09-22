def quant_palavras(frase):
    """Funçao que retorna o numero de palavras de uma frase dada"""
    frase = str.split(frase)
    palavras = str.count (frase, " ") + 1
    return palavras