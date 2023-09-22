"""o objetivo da função é responder a quantidade de palavras contidas
numa frase
"""
def quant_palavras(frase):
    frase = str.split(frase)
    frase = len(frase)
    return frase