import math
def carros(passageiros,cap=5):
    carro=math.ceil(passageiros/cap)
    '''
    Função que retorna a quantidade de carros para
    carregar determinada quanidade de pessoas:
    int, int -> int
    '''
    return carro