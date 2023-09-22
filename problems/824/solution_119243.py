def uppCons (x):
    y = ""
    for z in x:
        if z in 'bcdfghjklmnpqrstvwxyz':
            y += str.upper(z)
        else:
            y += z
    return y