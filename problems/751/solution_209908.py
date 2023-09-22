def quant_palavras(frase):
    """dada uma string contendo uma frase de entrada, retorna quantas palavras as frase possui
    str --> int"""
    frase_Separada=str.split(frase,' ')
    return len(frase_Separada)