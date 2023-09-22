def uppCons (texto):
    x=list(texto)
    for k in range(0,len(x)):
        if x[k] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(x[k])
    a=str(x).strip('[]')
    return a