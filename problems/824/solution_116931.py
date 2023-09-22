def uppCons (texto):
    x=list(texto)
    for k in range(0,len(x)+1):
        if x[k] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(x[k])
    return x[k]