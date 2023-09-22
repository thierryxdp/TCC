#Start your python function here
filtra_pares = [a, b, c, d]
a = int
b = int
c = int
d = int
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    list(filter(par,filtra_pares))