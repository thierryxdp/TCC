from math import floor
def bolos (A=2,B=3,C=5):
    '''função que define a quantidade exata de bolos
    que João deverá fazer com A xícaras de farinha,
    B ovos e C colheres de sopa de leite'''
    return min((A/2)+(B/3)+(C/5))