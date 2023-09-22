import string

def quant_palavras(frase):
    """Esta função retorna o número de palavras contidas na frase.
       String --> int"""
    
    for c in "!@#$%*()<>:|/?":
    frase = frase.replace(c, " ")