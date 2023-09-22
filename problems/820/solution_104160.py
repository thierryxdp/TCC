def posLetra(x,y,z):
    A = str.count(x, y)
    for letra in x:
        if A<z:
            return -1
        elif letra == y:
            return x.find(y)