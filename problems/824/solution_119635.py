def uppCons(f):
    
    for i in range(len(f)):
        if f[i] in 'bcdfghjklmnpqrstvxyzç':
            f = f[:i] + str.lower(f[i]) + f[i+1:]
    
    return f