import math
def carros(p,c=5):
    '''calculo da quantidade de carros necessarios para transportar todas as pessoas
    respeitando a capacidade maxima, sendo p=numero de pessoas e c=capacidade maxima
    a capacidade maxima normalmente é de 5, podendo ser dado uma entrada em caso de
    outros veiculos
    int,int->int'''
    return math.ceil(p/c)