"""Retorna a quantidade de palavras em uma frase.
 string -> int"""
def quant_palavras(frase):
    return (str.count(frase, " ")) + 1