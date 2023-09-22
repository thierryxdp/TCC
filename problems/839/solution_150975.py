import math
def carros(p:int,l:int=5)->int: 
    """essa função retorna o número de 
    carros que serão usados"""
    return int(math.ceil(p/l))