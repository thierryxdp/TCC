import math
def carros(n,p):
    '''funçao q recebe o numero de passageiros e de assentos em um veiculo
        e retorna a quantidade de carros que serao nescessarios para completar
        levar a todos
        int -> int
        exercicio 2'''
    return  math.ceil(p/n)