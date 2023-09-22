def quant_palavras(frase):
    """Retorna o número de palavras da frase."""
    """frase-> str"""
    frase = str.strip(frase,' ')
    frase_etapa2 = str.split(frase, ' ')
    
    return len(frase_etapa2)