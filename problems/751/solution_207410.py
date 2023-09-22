def quant_palavras(frase):
    """Dado uma frase, a função retorna a quantidade de palavras desta frase
    str -> int"""
    palavras = str.split(frase)
    return len(palavras)