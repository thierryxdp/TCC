from math import floor
def bolos(a,b,c):
    '''retorna a quantidade de bolos que João consegue fazer
    dados os ingredientes: (a)xícaras de farinha, (b)ovos e
    (c)colheres de sopa de leite'''
    return min({int(a/2), int(b/3), int(c/5)})