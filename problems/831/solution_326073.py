import math
def soma():

    """ Função que calcula a seguinte soma com precisão de duas casas:

        S = 10/1! - 9/2! + 8/3! - .... - 1/10!

    """

    numerador = 10

    S = 0


    for fatorial in range(1,11):

        S = (S + numerador/math.factorial(fatorial))*(-1)
        
        numerador = numerador - 1

    return round(S,2)