def total(l,d):
    for elementos in l:
        d[elementos]= dict.get(d,elementos,0)+1
    return d