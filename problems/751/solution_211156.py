def quant_palavras(frase):
    """conta quantas palavras tem na frase
    str->int"""
    separador = str.split(frase)
    contagem_final=len(separador)
    return contagem_final