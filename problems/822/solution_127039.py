def repetidos(l):
    ''
    list.sort(l)
    c=0
    prox=0
    while prox<len(l):
        if l[prox]==l[pp]:
            c=c+1
        prox=prox+1
    return c