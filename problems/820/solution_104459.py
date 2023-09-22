def posLetra(string, c, n):
    o = 0
    for i in range(len(string)):
        if string[i] == c:
            o += 1
        if o == n:
            return c
    return -1