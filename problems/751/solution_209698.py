def quant_palavras(frase):
    """Funcao que dada uma frase, retorna o numero de palavras da mesma.
    str -> int"""
    
    palavras = str.split(frase)
    
    return len(palavras)