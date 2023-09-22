from math import *

def bolos (A, B, C):
    """calcula a quantidade de bolos possíveis de serem preparados a partir do número de xícaras de farinha de trigo 
       (A), ovos (B) e colheres de sopa de leite (C) disponíveis, considerando que 2,3 e 5 são as quantidades neces-
       sárias de cada item, respectivamente, no preparo de um bolo
       int, int, int -> int"""
    return min(A/2, B/3, C/5)