def quant_palavras(frase):
    """Esta função retorna o número de palavras contidas na frase.
       String --> int"""
    
    for caractere in "!@#$%*()<>:|/?":
    frase = frase.replace(caractere, "")