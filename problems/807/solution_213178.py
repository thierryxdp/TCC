def conta_frases(texto):
    s=texto
    
    for x in ['!']:
        b=str.count(s,x)
    for x in ['?']:
        c=str.count(s,x)
    for x in ['.']:
        d=str.count(s,x)
    if d>1:
        return b+c+d//3
    elif d==1:
        return b+c+d