import math
def soma ():
    '''
    funcao que calcula a funcao proposta.
    str->float.
    '''
    soma = 0
    lista = [1,2,3,4,5,6,7,8,9,10]
    for num in range (10):
        soma = soma+((10/math.factorial(1))-(9/math.factorial(2))+(8/math.factorial(3))-(7/math.factorial(4))+(6/math.factorial(5))-(5/math.factorial(6))+(4/math.factorial(7))-(3/math.factorial(8))+(2/math.factorial(9))-(1/math.factorial(10)))/10
    return round(soma,2)