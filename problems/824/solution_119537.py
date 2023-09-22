def uppCons(s):
    s = list(s)
    for i in s:
        if i in 'bcdfghjklmnpqrstvwxyz':
            str.upper(i)
    return s