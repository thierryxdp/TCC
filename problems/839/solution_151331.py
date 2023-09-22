import math
def carros(p,c=5):
    '''calcula quantos veículos iguais precisa paara transportar um numero de pessoas
       float,float - > float'''
    return math.ceil(p/c)