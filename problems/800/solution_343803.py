def total(L, D):
    p = 0
    for i in L:
        if i in D:
            p += D[i]
        else:
            p += 0
    return p