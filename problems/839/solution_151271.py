from math import ceil
def carros(n,l=5):
    return n//l+ceil(n%l)