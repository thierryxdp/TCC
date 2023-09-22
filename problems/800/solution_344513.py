def total(c,p):
    i = 0.0
    for x in c:
        if x in p:
            i = i + dict.get(p,x)
    return round(i,2)