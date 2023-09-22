from math import *
def bolos (a,b,c):
    '''Calcula e retorna a quantidade maxima de bolos
que joao consegue fazer com certa xicara de farinha de 
trigo(a),ovos(b) e colheres de sopa de leite(c)'''
    y= floor(min(a/2,b/3,c/5))
    return y