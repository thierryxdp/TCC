import math

def carros(p,c=5):
    '''calcula a quantidade de veiculos necessarios para a viagem, dados o numero de passageiros p e caso o carro nao seja um convencional com 5 lugares, dar a sua capacidade c;
       int, int-> int'''
    return math.ceil(p/c)