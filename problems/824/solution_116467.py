def uppCons(f):
    f=list(f)
    i=0
    while i<len(f):
        if f[i] in 'BCDFGHJKLMNPQRSTVWXYZÇbcdfgçhjklmnpqrstvwxyz':
            f[i]=f[i].upper()
        i=i+1
    return "".join(f)