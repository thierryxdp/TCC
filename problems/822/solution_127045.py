def repetidos(l):
    ''
    list.sort(l)
    c=0
    prox=0
    pp=1
    while prox<len(l) and pp==len(l):
        if l[prox]==l[pp]:
            c=c+1
        prox=prox+1
        pp=pp+1
    return c