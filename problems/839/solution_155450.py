import math
def carros(pessoas, capacidade=5):
    '''calcula quantos veículos são necessários para
    transportar um dado número de pessoas, caso a
    capacidade do veˆculo em mente não for o 
    convencional (5 lugares), inserir tambem a 
    capacidade.
    int, int -> int'''
    return math.ceil(pessoas / capacidade)