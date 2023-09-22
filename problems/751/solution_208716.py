def quant_palavras(frase):
    """Função que retorna o número de palavras em uma frase
    str=>int"""
    lista = str.split(frase)
    num_palavras = len(lista)
    return num_palavras