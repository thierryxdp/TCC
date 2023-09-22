import math
def carros(np, na=5):
    """
    Descrição: Calcula e retorna o numero de carros com numero de assentos
    na necessarios para levar um certo numero de pessoas np em uma viagem

    Parâmetros:
        na -> int
        número de amigos
        
    Retorno:
        Quantidade de carros -> int
    """
    return math.ceil(np/na)