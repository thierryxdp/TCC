import math
def carros(x,y=5):
    '''calcula a quantidade de carros necessaria para uma viagem 
    a partir do numero de pessoas "x" e a capacidade do carro "y".'''
    return math.ceil(x/y)