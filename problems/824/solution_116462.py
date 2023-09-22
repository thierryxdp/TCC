def uppCons(f):
    f=list(f)
    i=0
    while i<len(f):
        if f[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            f[i]=str(f[i])
            f[i]=f[i].upper()
        i=i+1
    return str(f)