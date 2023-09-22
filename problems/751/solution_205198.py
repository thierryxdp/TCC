""" Recebe uma frase e retorna a quantidade de palavras da frase"""
"""string -> int"""
def quant_palavras(frase):
    frase.strip()
    return len(frase.split())