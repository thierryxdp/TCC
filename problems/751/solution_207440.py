# string -> int
def quant_palavras(frase):
"""Função que recebe uma string separa ela caso houver espaço(split) posteriormente conta a quantidade de palavras"""
    X = frase.split()
    return len(X)