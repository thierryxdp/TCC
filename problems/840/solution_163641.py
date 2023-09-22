import math
def bolos(disp_farinha, disp_ovo, disp_leite):
    '''Calcula a quantidade de bolos que é possivel se fazer com as medidas disponiveis de cada ingrediente.
    int, int, int -> int'''
    return min(math.floor(disp_farinha/2),math.floor(disp_ovo/3),math.floor(disp_leite/5))