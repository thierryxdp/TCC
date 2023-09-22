def uppCons(x):
    x_maiusculo = ' '
    for e in x:
        if e in 'bcdfghjklmnpqrstvwxyz':
            e = str.upper(x)
            x_maiusculo = x_maiusculo + e
    
    return x_maiusculo