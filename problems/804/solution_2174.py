#Start your python function here
def filtra_pares(x):
    """A função apartir de uma tupla com quatro elementos inteiros retorna uma outra tupla 
    com apenas elementos pares.tuple--tuple"""
    par=()
    a,b,c,d = x
    if a%2 == 0:
        par = par + (a,)
    if b%2 == 0:
        par = par +(b,)
    if c%2 == 0:
        par = par + (c,)
    if d%2 == 0:
        par = par + (d,)
    return par