def repetidos(l):
    f=1
    g=0
    h=0
    for e in l:
        if l[f] == l[h]:
            g = g + 1
    	f = f + 1
        h = h + 1
    return g