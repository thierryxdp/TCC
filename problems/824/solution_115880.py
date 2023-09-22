def uppCons(a):
    b = list(a)
    t = 0
    while t < len(b):
        if b[t] in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ':
            b[t].upper()
        t = t+1
    return list.sum(b)