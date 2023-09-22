#Para calcular a quantidade de carros necessária para
#levar P pessoas com um carro de C capacidade
#é necessário dividir P/C e arredondar para cima caso dê um float
def carros(P,C=5):
    """Calcula o número exato de carros necessários para levar
    P pessoas em um carro com C capacidade; int, int -> int"""
    import math
    c=P/C
    return math.ceil(c)