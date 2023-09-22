import math

def carros(np,np1=1):
    "função que calcula o numero exato de carros necesserarios pelo numero de pessoas(int,int->int)"
    nc = math.ceil(np+np1/5)
    return nc