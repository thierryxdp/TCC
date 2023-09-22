import math
def carros(p: int, c:int = 5) -> int:
    '''Calcula e retorna o número de carros necessários para
    transportar um número p de pessoas em carros de
    capacidade c'''
    return math.ceil(p/c)