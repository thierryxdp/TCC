def repetidos(l):
    c = 0
    for i in l:
        if i[x] == i[x-1]:
            c = c + 1
    return c