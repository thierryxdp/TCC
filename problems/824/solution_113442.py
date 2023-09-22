def uppCons(f):
    
    i=0
    fn = ''
    while i<len(f):
        if f(i) in 'bcdfghjklmnpqrstvwxz':
            fn += str.upper(f[i])
        else:
            fn += f[i]
        i += 1
    return fn