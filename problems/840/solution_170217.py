import math
def bolos (A,B,C):
    '''c'''
    A <= B or A <= C =A
    B <= A or B <= C =B
    return math.floor((((A/2)+(B/3)+(C/5))/3))//1