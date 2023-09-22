def quant_palavras(frase):
    """Função que, dada uma frasa, diz a quantidade pe palavras que ela tem.
    string -> int"""
    palavras = str.count(str.split(frase))
    return palavras