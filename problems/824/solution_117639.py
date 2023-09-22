def uppCons(frase):
    n=''
    t=0
    while t<len(frase):
        con=frase[t]
        if con in 'bcdfghjklmnpqrstvwxyzç':
            con=str.upper(con)
        n+=con
        t+=1
    return n