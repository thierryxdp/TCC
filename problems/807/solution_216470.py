def quant_palavras(frase):
    frase = frase.count('.') + frase.count('?') + frase.count('!')+frase.count('…')
    return frase