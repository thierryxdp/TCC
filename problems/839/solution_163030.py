import math
def carros(p,v=4):
   '''calcula o numero de carros necessarios para transportar os passageiros'''
   auto=math.ceil(p/v)
    return auto