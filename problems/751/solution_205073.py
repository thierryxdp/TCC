def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    # string -> int
    a = str.strip(frase)
    return str.count(a,' ') + 1