from math import ceil

def carros(pessoas, cap=5):
    y = pessoas % cap
    return ceil(y)