def uppCons (texto):
    x=list(texto)
    for k in range(0,len(x)+1):
        if x[k] in 'bcdfghjklmnpqrstvwxyz':
            return str.upper(x[k])