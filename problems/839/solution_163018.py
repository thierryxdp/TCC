def carros(p,v=4):
import math  
'''calcula o numero de carros necessarios para transportar os passageiros'''
    return int p/v
   v= math.ceil(p/v)
    return v