def quant_palavras(frase):
    """Função que dada ima frase, retorna o número de palavras da mesma. str -> int"""
    numero_palavras = str.split(frase)
    return len(numero_palavras)