import math     
def carros(pessoas, carro=5):
    ''' funcao que calcula quantos carros precisa dependendo da quantidade
    de pessoas no grupo que vai viajar 
    int -> int'''
    return math.ceil(pessoas/carro)