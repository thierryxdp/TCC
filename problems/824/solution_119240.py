def uppcCons (x):
    y=''
    for z in x:
        if z in 'bcdfghjklmnpqrstvwxyz':
            y += z
    return y