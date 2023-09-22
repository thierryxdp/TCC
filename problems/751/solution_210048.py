def quant_palavras(frase):
    """Retorna o número de palavras da frase."""
    """frase-> str"""
    frase = strip(frase,'')
    frase_etapa2 = slipt(frase, ' ')
    
    return len(frase_etapa2)