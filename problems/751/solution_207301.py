def quant_palavras(frase):
    """Dado  uma  frase retorna o número de palavras da frase;str, -> int"""
    frase = str.strip(frase)
    frase_l = str.split(frase)
    return len(frase_l)