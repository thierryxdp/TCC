import math
def carros(p,c=5):
    '''calcula o número de carros necessários para comportar certo número
    de pessoas (p), sendo a capacidade de cada carro(c), tendo como
    padrão(default) 5 pessoas por veículo.
    int,int-->int'''
    return math.ceiling(p/c)