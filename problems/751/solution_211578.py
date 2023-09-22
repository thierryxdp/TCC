# questão 1
from audioop import reverse
from re import L


def quant_palavras(frase):
    """Esta funcao recebe uma string e conta o numero de palavras nesta string
    str -> int"""
    numero_palavras = str.split(frase)
    return len(numero_palavras)