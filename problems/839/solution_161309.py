import math
def carros(num_pessoas,num_carros,c=5):
    """Clacular o numero exato de carros necessarios 
    para viajar dados o numero de pessoas"""
    return math.ceil(num_pessoas//num_carros,5)