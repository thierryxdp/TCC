def repetidos(l):
    ''
    c=0
    list.sort(l)
    prox=0
    while prox<len(l):
        if l[prox]==l[prox+1]:
            c=c+1
        prox=prox+1
    return c