def colchao(medidas,H,L):
    medidas[0] = a
    medidas[1] = b
    medidas[2] = c
    aux = 0
    if (a > b):
        aux = a
        a = b
        b = aux
    if (b > c):
        aux = b
        b = c 
        c = aux
    if (a > b):
        aux = a 
        a = b
        b = aux
    if (l > h):
        aux = h
        h = l
        l = aux
    if (l >= a):
        return True
    if (h >=b):
        return True
    else:
        return False