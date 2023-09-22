def uppCons(s):
    a = []
    s = list(s)
    for i in s:
        if i in 'bcdfghjklmnpqrstvwxyz':
            str.upper(i)
    s = str.join(s,)        
    return s