from numpy import sign
def carros(n,l=5):
    return n//l+sign(n%l)