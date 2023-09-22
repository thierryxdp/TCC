def uppCons(f):
    
    i=0
    while i<len(f):
        if f[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz': 
            f[i]=str.replace(f,f[i],str.upper(f[i]),i)
        i=i+1
    return f