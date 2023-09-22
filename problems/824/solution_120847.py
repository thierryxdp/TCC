def uppCons(f):
    saida=''
    i=0
    while i==len(f)-1:
        if f(i) in 'bcdfghjklmnpqrstvwxyz':
            saida=str.replace(f,f(i),str.upper(f(i)))
        i=i+1
    return saida