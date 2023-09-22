def quant_palavras(frase):
    """Função que conta quantas palavras tem uma frase, dada a frase a ser contada.
    frase -> str
    return -> int"""
    
    frase = frase.strip().split(' ')
    
    return len(frase)