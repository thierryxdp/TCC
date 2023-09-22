import math
def bolos (A,B,C):
    '''Calcula a quantidade máxima, inteira, de bolos dados os ingredientes'''
    return math.ceil(((A/2)+(B/3)+(C/5))/3)