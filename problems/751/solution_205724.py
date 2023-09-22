def quant_palavras(frase):
    """Dado uma string frase, retorne o número de palavras; string -> int"""
    if frase[0]==' ':
        return str.split(frase,' ')
    elif frase[-1]==' ':
        return str.split(frase,' ')
    s=str.count(frase,' ')
    return s+1