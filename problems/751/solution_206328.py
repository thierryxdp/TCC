""" função onde a entrada é uma string e ele retorna a quantidade de palavras na frase"""
"""string > int"""
def quant_palavras(frase):
    f = frase.split()
    return len(f)