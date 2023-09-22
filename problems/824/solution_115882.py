def uppCons(a):
    t = 0
    while t < len(list(a)):
        if list(a)[t] in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ':
            list(a)[t].upper()
        t = t+1
    return sum(list(a))