def uppCons(f):
    
    i=0
    while i<len(f):
        if f[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            
            str.upper(f[i])
        i=i+1
    return f