def repetidos(l):
    a = 1
    c = []
    while a <= (len(l) -1):
        if l[a] == l[a-1]:
            c.append(1)
        a = a+1
    return sum(c)