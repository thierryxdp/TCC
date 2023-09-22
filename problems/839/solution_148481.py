def carros(x):
    """ Calcula o número de carros (:int) necessários para transportar o número(n: int) de
pessoas em cada veículo. Se x<= 5, 1 carro necessário; se x> 5, usar x//5"""
    if 1<=x<=5:
        return 1
    elif x==0:
        return 0
    elif x>5 and 1<=y<=4:
        return x//4
    if x>5 and 5<=y<10:
        return x//y