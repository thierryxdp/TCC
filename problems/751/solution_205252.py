def quant_palavras(frase):
    """função que dada uma frase como parâmetro, calcula e retorna a quantidade de palavras que a frase possui
    str->int"""
    return len((str.split(str.strip(frase))))