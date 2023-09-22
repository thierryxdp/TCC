# A função retorna o número de palavras da frase.
# string -> int
def quant_palavras(frase):
    frase = str.split(frase)
    return len(frase)