def conta_frases(texto):
    s=texto
    for x in ['...']:
        a=str.count(s,x)
    for x in ['!']:
        b=str.count(s,x)
    for x in ['?']:
        c=str.count(s,x)
    for x in ['.']:
        d=str.count(s,x)
        ['...']=!['.']
        return a+b+c+d