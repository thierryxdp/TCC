def repetidos(l):
    l = []
    i = 1
    x = 0
    while i < len(l):
        if l[i] == l[i-1]:
            r = x + 1
        i = i + 1
    return r