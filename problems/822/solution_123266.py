def repetidos(l):
    i = 1
    r = 1
    while i < len(l):
        if l[i] == l[i-1]:
            r = r + 1
        i = i + 1
    return x