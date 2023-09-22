import math

def carros(p, cap=5):
    """caalcula quantos veiculos serao necessarios para uma viagem;
    int, int -> int"""
    return  math.ceil(p/cap)