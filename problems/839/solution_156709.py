import math
def carros(p , v=5)
''' Função que determina quantos veículos (v, padrão 5) são necessários para transportar (p) pessoas. '''
carros = math.ceil(p / v)
return carros