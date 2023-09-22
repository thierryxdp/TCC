import math
def carros(pessoas,maxcapacidade=5):
    '''calcula o numero de carros necessarios 
    para viagem, dado o numero de pessoas e a 
    capacidade maxima do carro, caso nao seja 
    informada a capacidade e adotado o valor 5
    int, int -> int'''
    return math.ceil(pessoas/maxcapacidade)