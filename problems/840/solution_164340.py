import math
def bolos(A,B,C):
    """A,B e C indicam respectivamente o número de xicaras de farinha, o numero de ovos e o numero de colheres de sopa de leite. A funcao calcula o numero maximo de bolos que pode ser feito, com essa quantidade de ingredientes."""
    return math.floor(min(A/2,B/3,C/5))