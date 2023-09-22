# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    z= (frase.count(".")+frase.count("?")+frase.count("!"))- 2*frase.count("...") + frase.count(" ")
    return z