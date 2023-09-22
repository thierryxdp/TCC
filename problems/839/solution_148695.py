import math
def carros(na):
    """
    Descrição: Calcula e retorna o numero de carros, com 5 assentos cada,
    necessarios para levar um certo numero na de amigos em uma viagem

    Parâmetros:
        na -> int
        número de amigos
        
    Retorno:
        Quantidade de carros -> int
    """
    return math.ceil(na/5)