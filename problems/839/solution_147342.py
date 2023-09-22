import math
def carros(x,c=5):
    '''Função que retorna o número de carros necessários para esta viagem, dados o número de pessoas x e a capacidade de cada carro c.
    Caso não seja informada a capacidade de cada carro, será utilizado o valor 5.
    int, int -> int'''
    return math.ceil(x/c)