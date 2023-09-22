def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    frase = str.strip(frase)
    palavras = str.count (frase, ' ') + 1
    return palavras