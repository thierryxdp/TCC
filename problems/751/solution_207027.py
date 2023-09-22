def quant_palavras(frase):
    """Retorna o numero de palavras que a frase fornecida contém
    str -> int"""
    
    quantidade = str.split(frase)
    
    return len(quantidade)