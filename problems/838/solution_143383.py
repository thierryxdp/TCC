import math
def num_bombons (a, b=2):
    """ Calcula o numero de bomboons que Pedrinho pode comprar com o bombom custando a e o dinheiro que ele tem sendo b, e b não pode ser 0, a>b"""
    return math.ceil(a/b)