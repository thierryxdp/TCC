def repetidos(ls):
    o=0
    for e in range(len(ls)):
        if ls[e]==ls[e+1]:
            o=o+1
    return o