def quant_palavras(frase):
    """Função que dada uma frase, retorne a quantidade de palavras.
    str -> int"""
    frase = input ("digite uma frase: ")
    frase1 = (frase.split(" "))
    return len(frase1)