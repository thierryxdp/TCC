# bolos
import math
def bolos (a,b,c):
    '''quantidade maxima de bolos possiveis onde na entrada a,b,c indicam respectivamente
    xícaras de farinhas de trigo, numero de ovos e colheres de sopa de leite
    retornando a quantidade maxima de bolos respeitando que se tenha o minimo de cada
    ingrediente
    float,float->int'''
    return min(math.floor(a/2),math.floor(b/3),math.floor(c/5))