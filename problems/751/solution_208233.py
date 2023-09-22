def quant_palavras(frase):
    """função que retorna um numero de palavras de uma frase"""
    """stg->int"""
    frase = str.strip(frase)
    frase = str.split(frase)
    return len(frase)