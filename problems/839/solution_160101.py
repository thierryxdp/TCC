def carros(p,c):
    '''Funcao que calcula o numero de carros, dados a quantidade de pessoas(p) e a capacidade do carro(c); int, int->int'''
    car = math.ceil(p/c)
    return car