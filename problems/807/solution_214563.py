def Num_Frases(texto):
    x=str.replace(texto,'...','.')
    y=str.replace(x,'?','.')
    z=str.replace(y,'!','.')
    f=str.split(z,'.')
    if z[len(z)-1]=='.':
        return len(f)-1
    else:
        return len(f)