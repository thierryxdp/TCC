def quant_palavras(frase):
    '''
    dada uma str como entrada, retorna quantas palavras
    a str possui
    dados de entrada: str
    retorna: int
    '''
    palavras = str.split(frase)
    return len(palavras)