def total(l,d):
    ''''''
    t=0
    for x in l:
        if x==d:
            t=t+d[x]
    return round(t,2)