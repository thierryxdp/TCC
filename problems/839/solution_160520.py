import math
def carros(x,y):
    """calcula quantos carros com capacidade de (y) lugares são necessários para levar um número (x) de pessoas
    int,int->float"""
    math.ceil(x/y)