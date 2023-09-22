def posLetra(x,y,z):
    A = str.count(x,y)
    for frase in x:
        if A < z:
            return -1