def faltante (nlist):
    tlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    missing = 0
    i = 0
    while i < len(tlist):
        if tlist[i] not in nlist:
            missing = tlist[i]
        i += 1
    return missing