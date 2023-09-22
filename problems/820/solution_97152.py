def posLetra(string,l,n):
    '''...'''
    x = 0
    for y in range(l(string)):
        if(string[y] == l):
            x += 1
        if (x == n):
            return y