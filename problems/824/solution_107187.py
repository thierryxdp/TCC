def uppCons(x):
    v=0
    while v<len(x):
        if x[v] in 'bcçdfghjklmnpqrstvxwyz':
            y=str.upper(x[v])
            x=str.replace(x,x[v],y)
        v=v+1
    return x