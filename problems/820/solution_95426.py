def posLetra(string, l, n):
    oc = 0
    posic = []
    h = 0
    c = 6
    for i in range(len(string)):
        if(string[i] == l):
            oc = oc + 1
            h = i
            list.append(posic, h)
    if n <= oc:
        c = posic[n-1]
    else:
        c = -1
    return c