def posLetra(string,letra,n):
    f = str.count(string,letra)
    if n > f:
        return -1
    else:
        x = 0
        y = 0
        while y < n:
            x = str.find(string,letra,x + 1)
            y = y + 1
        return x