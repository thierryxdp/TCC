def uppCons(f):
    saida=f
    i=0
    while i<len(f):
        if f[i] in 'bcdfghjklmnpqrstvwxyzç':
            saida=str.replace(saida,f[i],str.upper(f[i]))
        i=i+1
    return saida