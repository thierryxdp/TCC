def quant_palavras(frase):
    """Esta é a função que dada uma frase retorna o número de palavras que ela possui, str -> int"""
    x= str(frase)
    y= str.split(x)
    return len(y)