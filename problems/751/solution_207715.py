def quant_palavras(frase):
    """Funcao que calcula e retorna o número de palavras do parâmetro
    (frase).
    str -> int"""
    splitador = frase.split()
    return len(splitador)