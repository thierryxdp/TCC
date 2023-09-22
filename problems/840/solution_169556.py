"""
2 xícaras de farinha
3 ovos
5 colheres de sopa de leite
Casa...
A xícaras de farinha 
B ovos
C colheres de sopa de leite
A = 2*x ---> A multiplo de 2
B = 3*y ---> B multiplo de 3
C = 5*z ---> C multiplo de 5
"""
from math import*
def bolos (A,B,C):
    return floor (min (A/2, B/3, C/5))