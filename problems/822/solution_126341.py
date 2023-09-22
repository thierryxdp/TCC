def repetidos (l):
    nl = []
    for x in l:
        if (l.count(x) > 1):
            nl.append(x)
    return nl