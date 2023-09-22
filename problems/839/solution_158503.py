"""
Nesta função usaremos o quanto de dinheiro há disponível para compra dos
bombons e dividir este valor pelo preço de cada bombom, encontrando assim
um valor inteiro do maior número de bombons.
float,float -> float
"""
import math
def carros(pessoas,assentos=5):
    x = pessoas/assentos
    return math.ceil(x)