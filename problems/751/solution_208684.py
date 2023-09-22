# contará o número de palavras dentro desta frase
# frase
# string -> int
def quant_palavras(frase):
    """uma funçao que dada uma frase a função contará o número de palavras dentro desta frase string->int"""
    removeSpaces = frase.strip()
    splitPhrase = removeSpaces.split()
    return len(splitPhrase)