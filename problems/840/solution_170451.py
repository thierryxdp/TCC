import math
def bolos(a,b,c):
    """Esta função calcula o máximo de bolos possíveis de serem feitos com os ingredientes dados, sendo (a) xícaras de leite, (b) ovos e (c) colheres de sopa de leite"""
    return math.floor((a/2)+(b/3)+(c/5))/3)