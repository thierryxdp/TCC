def uppCons(frase):
    r=[]
    for e in list(frase):
        if 'bcdfghijklmpqrstvwxyz' in frase:
            e=str.upper(e)
    return frase