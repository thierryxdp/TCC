# Dada a string frase, esta função retorna a qunatidade de palavras contidas
# na string.
# string -> int
def quant_palavras(frase):
    frase = str.strip(frase)
    cont = frase.count(' ') + 1
    return cont