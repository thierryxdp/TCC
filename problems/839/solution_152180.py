def carros(p,c=5):
    """calcula o número de carros necessários para comportar
    um número P de passageiros, sendo a capacidade C igual a 
    5 quando não informada"""
    return math.ceil(p/c)