def quant_palavras(frase):
    """Função que, dada uma frasa, diz a quantidade pe palavras que ela tem.
    string -> int"""
    palavras = str.split(frase)
    quantidade = str.count(palavras)
    return palavras