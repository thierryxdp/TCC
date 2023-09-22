def quant_palavras(frase):
    """Retorna o número de palavras da frase dada; str -> int"""
    frase=str.replace(frase, ',','')
    frase=str.replace(frase, '!','')
    frase=str.replace(frase, '?','')
    frase=str.replace(frase, '-','')
    frase=str.replace(frase, '.','')
    frase=str.split(frase)
    return len(frase)