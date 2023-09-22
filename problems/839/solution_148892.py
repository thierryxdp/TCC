'''O programa recebe como entrada número de pessoas e diz quantos carros serão necessários. 
O número de assentos padrão de cada carro é 5, porém, caso trate-se de carros de arranjo 
diferente de assentos, deve ser especificado.'''
def carros(passageiros, assentos = 5):
    import math
    return math.ceil(passageiros/assentos)