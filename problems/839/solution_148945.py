def carros(p,c=5):
    '''Calcula e retorna a quantidade de carros de capacidade c
       para transportar um número p de pessoas'''
    return math.ceil(p/c)