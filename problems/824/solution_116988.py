def uppCons(f):
    ''
    f=list(f)
    prox=0
    v='aAeEiIoOuU'
    while prox<len(f):
        if f[prox] not in v:
            str.upper(f[prox])
        prox=prox+1
        return f