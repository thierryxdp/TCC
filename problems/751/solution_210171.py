def quant_palavras(frase):
    """função que retorna a quantidade de palavras contidas
    em uma frase, dada a frase como entrada
    string -> int"""
    frase_separada = str.split(frase)
    return len(frase_separada)