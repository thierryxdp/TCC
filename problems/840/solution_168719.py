from math import *

def media_pesos(qtd1,qtd2,p1=3,p2=2):
    """
        Retorna a média dos pesos ponderados
        : param qtd1: float
        : param qtd2: float
        : param p1: float
        : param p2: float
        : return: float
    """
    """
        Retorna a média dos pesos ponderados
        float, float, float, float -> float
    """
    """
        Retorna a média dos pesos ponderados
        Parâmetros:
            entrada:
                qtd1,qtd2,p1,p2: float
            saída:
                float
    """
    return (qtd1*p1+qtd2*p2)/(p1+p2)