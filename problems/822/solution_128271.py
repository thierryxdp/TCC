def repetidos(l):
    i=0
    r=0
    for x in l:
        if x==l[i-1]:
            r=r+1
    return r