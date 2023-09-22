def posLetra(string, l, n):
    i = 0
    j = 0
    z = 0
    while i < len(string):
        if l in string[i]:
            j += 1
            z = i
            i += 1
            if j == n:
                break          
        else:
            i += 1
    if j == n:
        return z
    else:
        return -1