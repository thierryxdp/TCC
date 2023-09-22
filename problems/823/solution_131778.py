def faltante(nlist):
    nlist.sort()
    list_c = list(range(nlist[0], nlist[len(nlist) - 1]))
    missing = 0
    i = 0
    while i < len(nlist):
        if list_c[i] not in nlist:
            missing = list_c[i]
        i += 1
    return missing