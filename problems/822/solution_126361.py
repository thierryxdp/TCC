def repetidos(l):
    c = 0
    a = 1
    while a < (len(l) - 1):
        if l[a] == l[a-1]:
            c = c + 1
    a = a + 1
    return c