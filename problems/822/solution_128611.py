def repetidos(ls):

    r = []
    for e in range(len(ls)):
        if ls[e]== ls[e-1]:
            r.append(ls[e])
    return len(r)