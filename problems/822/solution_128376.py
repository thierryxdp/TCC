def repetidos (l):
    o = 0
    L = l
    F = del l[0]
    for n in range(len(F)):
        if L[n] == F[n]:
            o += 1
       
    return o