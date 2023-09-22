def uppCons(f):
    
    i=0
    while i<len(f):
        if f[i] in 'bcdfghjklmnpqrstvwxyz'and  str.isupper(f[0]):
            
            str.upper(f[i])
        i=i+1
    return f