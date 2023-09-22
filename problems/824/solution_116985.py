def uppCons(f):
    ''
    f=list(f)
    prox=0
    v='aeiou'
    while prox<len(f):
        if f[prox] not in v:
            str.upper(f[prox])
        prox=prox+1