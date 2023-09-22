def quant_palavras(frase:str)-> int:
    """Retorna o número de palavras da frase dada"""
    palavras= str.split(frase, ' ')
    return len(palavras)