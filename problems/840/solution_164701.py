from math import floor
def bolos(farinha, ovos, leite):
    '''Calcula o número de bolos que podem ser feitos com determinada 
    quantidade de farinha de trigo, de ovos e de leite
    int, int -> int'''
    return float(min(farinha / 2), (ovos / 3)  (leite / 5) )