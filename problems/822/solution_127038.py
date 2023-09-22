def repetidos(l):
    ''
    c=0
    list.sort(l)
    prox=0
    pp=1
    while prox<len(l):
        if l[prox]==l[pp]:
            c=c+1
        prox=prox+1
        pp=pp+1
    return c