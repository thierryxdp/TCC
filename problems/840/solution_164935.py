import math
def farinha(a):
    return math.floor(a/2)
def ovos (b):
    return math.floor(b/3)
def leite (c):
    return math.floor(c/5)
def receita (a,b,c):
    return math.floor((farinha(a)+ovos(b)+leite(c))/3)