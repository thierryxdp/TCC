#->float
from import math.factorial
def soma_h():
    "Fução que calcula a soma de um inteiro fatorial e retorna o resultado com 2 casas decimais."
    soma=0
    denominador=1
    for numerador in range(10,0,-1):
        soma+=float(numerador)/factorial(denominador)
        denominador+=1
    return round(soma,2)