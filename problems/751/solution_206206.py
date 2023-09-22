def quant_palavras(frase):
    """Dada uma string, essa função nos diz a quantidade de palavras presentes na mesma; string -> int"""
    list_palavras = str.split(frase)
    return len(list_palavras)