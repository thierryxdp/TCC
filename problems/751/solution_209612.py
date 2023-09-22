def quant_palavras(frase):
    """Essa função retira os espaços do meio e do final e devolve
    a quantidade de palavras que há na frase"""
    palavras= list.strip(frase)
    return len(palavras)