def uppCons(a):
    b = list(a)
    t = 0
    while t < len(b):
        if b[t] in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ':
            list.remove( b, t )
            
        t = t+1
    return "".join(b)