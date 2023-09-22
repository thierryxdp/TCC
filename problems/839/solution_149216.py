import math
def carros(p, l=5):
    '''calcula quantos carros sao necessarios para transpotar um numero p
    de pessoas em um veiculo com l lugares
    se o argumento l nao for preenchido serao considerados 5 lugares
    int, int -> int'''
    return math.ceil(p/l)