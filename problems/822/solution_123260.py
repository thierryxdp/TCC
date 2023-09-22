def repetidos(l):
    i = 1
    r = x
    while i < len(l):
        if l[i] == l[i-1]:
            r = x + 1
        i = i + 1
    return r