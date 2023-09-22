def posLetra(string, l, n):
    oc = 0
    posic = []
    h = 0
    for i in range(len(string)):
        if(string[i] == l):
            oc = oc + 1
            h == i 
            posic.append(h)
        if n < oc:
            c = posic[n]
        else:
            c = -1
    return c