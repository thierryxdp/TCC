import math
def carros (n, c = 5):
"""Calcula quantos carros são necessarios para transportar um número n de passageiros"""
return math.ceil (n/c)