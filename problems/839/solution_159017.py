import math
def carros(pessoas, carros=5):
    
    '''calcula a quantidade de carros necessarios para viajar
    dada a quantidade de pessoas e capacidade dos carros.
    Caso nao dada a capacidade será considerada o convencial de 5 assentos.
    Int, Int -> Int'''
    
    return math.ceil (pessoas/carros)