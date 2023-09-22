# define o numero de palavras que uma frase tem
# variavel -> frase
# string -> int
def quant_palavras(frase):
    """DEFINE QUANTAS PALAVRAS TEM A FRASE,ENTRADA-> FRASE , SAIDA -> INT DE PALAVRAS"""
    return str.count (str.split(frase))