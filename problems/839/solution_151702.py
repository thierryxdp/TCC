def carros (x,y):
'''função que calcula o numero de carros necessarios para a viagem, divividno o numero de pessoas (x) pelo capacidade do carro (y)'''
import math
carros=x/y
carros=math.ceil(carros)
return carros = x/y