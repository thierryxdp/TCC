def posLetra(string, l, n):
    x = string.find(l)
    while x>= 0 and n>1:
        x = string.find(1, x + 1)
        n-= 1 
    return x