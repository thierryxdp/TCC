def carros(n, c=5):
    if n%c==0:
        return n/c
    return n//c + 1