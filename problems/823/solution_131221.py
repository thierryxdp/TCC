def faltante(l):
    a = max(l)
    i = 1
    total = sum(l)
    real = a
    while i <= a:
        real = real + (a-i)
        i = i+1
    z = real - total
    if z == 0:
        z = z + a +1 
    return z